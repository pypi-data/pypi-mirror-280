import datetime
import logging
from typing import List, Optional
from sqlalchemy import select


from caerp.compute.math_utils import percent, percentage, floor_to_precision

from caerp.models.price_study import PriceStudyChapter, PriceStudyProduct
from caerp.models.price_study.base import BasePriceStudyProduct
from caerp.models.price_study.price_study import PriceStudy
from caerp.models.task import TaskLine, TaskLineGroup, Invoice, CancelInvoice
from caerp.models.tva import Tva
from caerp.models.task.services.invoice import InvoiceService

from caerp.controllers import base

logger = logging.getLogger(__name__)


class EstimationInvoicingController(base.BaseController):
    """
    Controller managing invoice generation for estimations

    Context is the estimation we're working with

    The amounts to invoice come from the business we're working with.
    We forget about the estimation's original PaymentLine configuration

    Handles both classic estimation and estimations with a price study
    """

    # NOTE : Pour produire les factures intermédiaires, nous devons calculer
    # les montants par taux de tva et comptes produits, afin de répartir le montant à
    # facturer sur chaque produit
    #
    # Dans le cas des devis multi tva avec remises, un traitement différencié
    # doit être effectué:
    # Soit une facture avec plusieurs taux de tva et une remise sur un de ces taux
    # 1000€ à 20% + 1000€ à 5.5% - 500€ à 20%
    # Acompte de 70% soit 1158.50€

    # Nous caclulons le pourcentage à appliquer sur les lignes sans remise pour la tva
    # à 20% et le pourcentage pour la tva à 5.5% :
    # 35% de 1000€ pour la tva à 20%
    # 70% de 1000€ pour la tva à 5.5%

    def __init__(self, context, request=None):
        super().__init__(context, request)
        self.multiple_tva = self.context.has_multiple_tva()
        self.has_discounts = len(self.context.discounts) > 0

    def _get_common_invoice(self, user) -> Invoice:
        """
        Prepare a new Invoice related to the given estimation

        :param obj estimation: The estimation we're starting from
        :param obj user: The user generating the new document
        :returns: A new Invoice/InternalInvoice
        :rtype: `class:Invoice`
        """
        params = dict(
            user=user,
            company=self.context.company,
            project=self.context.project,
            phase_id=self.context.phase_id,
            estimation=self.context,
            payment_conditions=self.context.payment_conditions,
            description=self.context.description,
            address=self.context.address,
            workplace=self.context.workplace,
            mentions=[mention for mention in self.context.mentions if mention.active],
            business_type_id=self.context.business_type_id,
            notes=self.context.notes,
            mode=self.context.mode,
            display_ttc=self.context.display_ttc,
            start_date=self.context.start_date,
            end_date=self.context.end_date,
            first_visit=self.context.first_visit,
            decimal_to_display=self.context.decimal_to_display,
            insurance_id=self.context.insurance_id,
            business_id=self.context.business_id,
        )

        invoice = InvoiceService._new_instance(
            self.request, self.context.customer, params
        )
        return invoice

    def _line_amounts_by_tva_and_product_native(self) -> dict:
        """
        Compute amounts by tva and product ids
        {tva: {product_id: amount,},}

        amount is an integer in the "native" format (HT/TTC)
        """
        if self.context.mode == "ht":
            method = "total_ht"
        else:
            method = "total"

        ret_dict = {}
        for line in self.context.all_lines:
            ret_dict.setdefault(line.tva, {}).setdefault(line.product, 0)
            ret_dict[line.tva][line.product] += getattr(line, method)()
        return ret_dict

    def _duplicate_estimation_lines(self, remove_cost: bool = False):
        """Produce a copy of the estimation lines
        :param bool remove_cost: Remove the cost from the lines (only for display purpose)
        """
        groups = []
        for group in self.context.line_groups:
            group = group.duplicate()
            if remove_cost:
                for line in group.lines:
                    line.cost = 0
            groups.append(group)
        return groups

    def _duplicate_estimation_discounts(self):
        """
        Produce a copy of the estimation discounts
        """
        result = []
        for discount in self.context.discounts:
            discount = discount.duplicate()
            result.append(discount)
        return result

    def _get_task_line(self, description, cost, tva, product_id) -> TaskLine:
        """
        Build a new TaskLine with the given parameters
        """
        line = TaskLine(
            cost=floor_to_precision(cost, precision=5),
            description=description,
            tva=tva,
            quantity=1,
            product_id=product_id,
        )
        line.mode = self.context.mode
        return line

    def _ensure_ratio_lower_than_100(self, amount_ratio):
        """
        Ensure the given ratio is lower or equal than 100%
        """
        return min(amount_ratio, 100.0)

    def _get_ratio_by_tva(self, amount_ttc: int) -> dict:
        """
        Transform an TTC amount into a ratio of the original estimation's TTC

        Build the ratio for each tva if needed
        """
        # Le montant ttc a été calculé depuis le ttc du devis
        # Pour calculer le pourcentage à utiliser dans la facture intermédiare :
        #  - Si pas de remise, on calcule le pourcentage depuis le *ttc du devis*
        #  - Si on a des remises, on ne les reproduit que dans la facture de solde, il
        #    faut donc calculer le pourcentage depuis le *ttc avant remise*
        #      - Si on a plusieurs tva, on calcule le pourcentage pour chaque
        #        taux de tva

        total = self.context.total()
        if total < amount_ttc:
            self.request.session.flash(
                "Attention : Le montant que vous voulez facturer est plus élevé que "
                "le montant du devis."
                "Le montant de la facture générée a été réduit et correspond au "
                "total du devis.",
                queue="error",
            )
        if not self.multiple_tva:
            # Les deux calculs ci-dessous sont censés être identiques
            # (mais on préfère être plus explicite)
            # 1- Si j'ai une remise, mon référentiel pour calculer le pourcentage
            # est le ttc avant remise (car les remises ne figurent pas dans
            # les factures intermédiaires)
            # 2- Pas de remise, je prends le ttc du devis
            if self.has_discounts:
                amount_ratio = percent(
                    amount_ttc, self.context.groups_total_ttc(), precision=5
                )
            else:
                amount_ratio = percent(amount_ttc, self.context.total(), precision=5)
            amount_ratio = self._ensure_ratio_lower_than_100(amount_ratio)
            return {"default": amount_ratio}

        else:
            # on convertit le montant à facturer en pourcentage du devis
            global_percentage = percent(amount_ttc, self.context.total(), precision=5)
            global_percentage = self._ensure_ratio_lower_than_100(global_percentage)
            result = {}
            ttc_by_tva = self.context.tva_ttc_parts()
            ttc_by_tva_without_discounts = self.context.tva_ttc_parts(
                with_discounts=False
            )
            # On calcule le pourcentage à appliquer sur les lignes avant remise
            # On doit donc différencier le cas de chaque tva
            for tva, ttc in ttc_by_tva.items():
                ttc_no_discount = ttc_by_tva_without_discounts[tva]
                if ttc_no_discount == ttc:
                    # Pas de remise
                    amount_ratio = global_percentage
                else:
                    # "pourcentage à appliquer sur les lignes avant remises" =
                    # "ttc pour cette tva" x "pourcentage global" / "ttc avant remise"
                    amount_ratio = ttc * global_percentage / ttc_no_discount
                result[tva] = amount_ratio
            return result

    def _intermediate_amounts_by_tva_and_product_native(
        self, amount_ratio_by_tva: dict
    ) -> dict:
        """
        Compute a dict of the amount to invoice for each product using the
        given ratio dict
        """
        amounts = self._line_amounts_by_tva_and_product_native()
        for tva, detail in amounts.items():
            amount_ratio = amount_ratio_by_tva.get(
                tva, amount_ratio_by_tva.get("default")
            )
            for product, amount in detail.items():
                amounts[tva][product] = percentage(amount, amount_ratio)
        return amounts

    def _get_intermediate_task_line_group(
        self, description, amount_ratio_by_tva: dict
    ) -> TaskLineGroup:
        """
        Produce a TaskLineGroup for an intermediate invoice

        Each TaskLine matches one of the original estimation's products
        Allow to have a coherent accounting information when exporting the invoice

        TaskLines are hidden in the pdf
        """
        amounts = self._intermediate_amounts_by_tva_and_product_native(
            amount_ratio_by_tva
        )
        group = TaskLineGroup(title=description, display_details=False)
        for tva, detail in amounts.items():
            for product, amount in detail.items():
                line = self._get_task_line(description, amount, tva, product.id)
                group.lines.append(line)

        return group

    def _get_price_study_chapter_from_task_line_group(
        self, task_line_group: TaskLineGroup
    ):
        """
        Convert a TaskLineGroup to a PriceStudyChapter.
        """
        chapter = PriceStudyChapter(
            title=task_line_group.title,
            description=task_line_group.description,
            display_details=False,
        )
        for line in task_line_group.lines:
            product = PriceStudyProduct(
                description=line.description,
                ht=line.cost,
                tva=Tva.by_value(line.tva),
                quantity=1,
                product_id=line.product_id,
            )
            chapter.products.append(product)
        return chapter

    def _gen_intermediate_chapters(
        self, price_study: PriceStudy, task_line_group: TaskLineGroup
    ) -> PriceStudy:
        """Generate the chapters of the intermediate invoice's price study"""
        # # On génère un chapitre pour la partie facturée
        chapter = self._get_price_study_chapter_from_task_line_group(task_line_group)
        price_study.chapters.append(chapter)
        self.request.dbsession.merge(price_study)
        self.request.dbsession.flush()
        # On synchronise les montants
        price_study.sync_amounts(sync_down=True)
        # On synchronise la facture avec les données de l'étude
        price_study.sync_with_task(self.request)

        return price_study

    def gen_deposit_invoice(
        self,
        user,
        description,
        deposit_ttc: int,
        date: Optional[datetime.date] = None,
        add_estimation_details: bool = True,
    ):
        """
        Generate a deposit invoice based on the current estimation

        :param obj user: The user generating the new document
        :param str description: The description of the invoice
        :param int deposit_ttc: The TTC amount expected for the invoice
        :param obj date: The date of the invoice
        :param bool add_estimation_details: Add the estimation lines to the invoice (with cost as 0€) ?

        :returns: A new Invoice / InternalInvoice
        :rtype: `class:Invoice`
        """
        return self.gen_intermediate_invoice(
            user, description, deposit_ttc, date, add_estimation_details
        )

    def gen_intermediate_invoice(
        self,
        user,
        description,
        amount_ttc: int,
        date: Optional[datetime.date] = None,
        add_estimation_details: bool = True,
    ) -> Invoice:
        """
        Generate an intermediate invoice based on the current estimation

        Also handles PriceStudy based invoicing

        :param obj user: The user generating the new document
        :param str description: The description of the invoice
        :param int amount_ttc: The TTC amount expected for the invoice
        :param obj date: The date of the invoice
        :param bool add_estimation_details: Add the estimation lines to the invoice (with cost as 0€) ?

        :returns: A new Invoice / InternalInvoice
        :rtype: `class:Invoice`
        """
        invoice: Invoice = self._get_common_invoice(user)

        if date is not None and invoice.date < date:
            invoice.date = date
        invoice.financial_year = invoice.date.year
        invoice.display_units = 0
        amount_ratio_by_tva = self._get_ratio_by_tva(amount_ttc)
        # The lines we actually charge
        intermediate_task_line_group = self._get_intermediate_task_line_group(
            description, amount_ratio_by_tva
        )
        if self.context.has_price_study():
            invoice._clean_task(self.request)
            if add_estimation_details:
                # On copie l'étude de prix du devis en mettant tout à 0
                new_price_study = self.context.price_study.duplicate(
                    force_ht=True, exclude_discounts=True, remove_cost=True
                )
            else:
                new_price_study = PriceStudy()
            new_price_study.task = invoice
            self._gen_intermediate_chapters(
                new_price_study, intermediate_task_line_group
            )
        else:
            if add_estimation_details:
                invoice.line_groups = self._duplicate_estimation_lines(remove_cost=True)
            else:
                invoice.line_groups = []
            invoice.line_groups.append(intermediate_task_line_group)

        invoice.cache_totals(self.request)
        self.request.dbsession.merge(invoice)
        self.request.dbsession.flush()
        return invoice

    def _get_existing_invoice_ids_query(self):
        if self.context.business_id:
            subquery1 = select(CancelInvoice.invoice_id).where(
                CancelInvoice.business_id == self.context.business.id
            )
        else:
            subquery1 = []
        return (
            select(Invoice.id)
            .where(Invoice.estimation_id == self.context.id)
            .where(Invoice.id.notin_(subquery1))
        )

    def _collect_already_invoiced_groups(self):
        """
        Collect all the TaskLineGroups already invoiced
        """
        invoice_id_query = self._get_existing_invoice_ids_query()
        subquery = (
            select(TaskLine.group_id)
            .join(TaskLine.group)
            .filter(TaskLineGroup.task_id.in_(invoice_id_query))
            .filter(TaskLine.cost != 0)
        )
        query = select(TaskLineGroup).where(TaskLineGroup.id.in_(subquery))
        return self.request.dbsession.execute(query).scalars().all()

    def _collect_already_invoiced_chapters(self) -> List[PriceStudyChapter]:
        """
        Collect all the PriceStudyChapter already invoiced
        """
        invoice_id_query = self._get_existing_invoice_ids_query()
        subquery = (
            select(BasePriceStudyProduct.chapter_id)
            .join(BasePriceStudyProduct.chapter)
            .join(PriceStudyChapter.price_study)
            .filter(PriceStudy.task_id.in_(invoice_id_query))
            .filter(BasePriceStudyProduct.total_ht != 0)
        )
        query = select(PriceStudyChapter).where(PriceStudyChapter.id.in_(subquery))
        return self.request.dbsession.execute(query).scalars().all()

    def gen_sold_price_study(self, invoice):
        """
        Generate a price study attached to the sold invoice compiling
        the estimation informations and the intermediary invoices
        """
        # On retrouve ce qui a déjà été facturé
        intermediate_chapters = self._collect_already_invoiced_chapters()

        # On crée une étude de prix sans les éléments de calcul (coef de marge
        # ...)
        price_study = self.context.price_study.duplicate(force_ht=True)
        price_study.task = invoice

        # On crée des produits d'étude pour acompte + paiements intermédiaires
        for invoiced_chapter in intermediate_chapters:
            other_invoice = invoiced_chapter.price_study.task
            title = ""
            if invoiced_chapter.title:
                title = f"{invoiced_chapter.title} - "
            title += f"Facture {other_invoice.official_number}" " du {}".format(
                other_invoice.date.strftime("%d/%m/%Y")
            )
            logger.debug(invoiced_chapter.id)
            chapter = PriceStudyChapter(
                title=title,
                description=invoiced_chapter.description,
                display_details=invoiced_chapter.display_details,
            )
            for invoiced_product in invoiced_chapter.products:
                if invoiced_product.ht != 0:
                    product = invoiced_product.duplicate(
                        from_parent=True, force_ht=True
                    )
                    product.ht = -1 * invoiced_product.ht
                    product.total_ht = -1 * invoiced_product.total_ht
                    if getattr(product, "items", None) is not None:
                        for item in product.items:
                            item.ht = -1 * item.ht
                            item.total_ht = -1 * item.total_ht
                    chapter.products.append(product)
            price_study.chapters.append(chapter)

        self.request.dbsession.merge(price_study)
        self.request.dbsession.flush()
        # On synchronise les montants
        price_study.sync_amounts(sync_down=True)
        # On synchronise la facture avec les données de l'étude
        price_study.sync_with_task(self.request)

        return price_study

    def gen_sold_invoice(self, user, date=None):
        """
        Generate a sold invoice based on the given estimation definition

        :param obj estimation: The estimation we're starting from
        :param obj user: The user generating the new document
        :returns: A new Invoice/Internal object
        :rtype: `class:Invoice`
        """
        invoice = self._get_common_invoice(user)

        if date and invoice.date < date:
            invoice.date = date
        invoice.financial_year = invoice.date.year
        invoice.display_units = self.context.display_units
        line_groups = []
        # Retrieve already invoiced lines

        if self.context.has_price_study():
            # On génère une étude de prix (sans les formules de calcul, direct en ht)
            # Et on génère les TaskLineGroup et TaskLine depuis l'étude
            invoice._clean_task(self.request)
            self.gen_sold_price_study(invoice)
        else:
            line_groups = self._duplicate_estimation_lines(remove_cost=False)

            task_line_groups = self._collect_already_invoiced_groups()
            if task_line_groups:
                for invoiced_group in task_line_groups:
                    other_invoice = invoiced_group.task
                    title = (
                        f"{invoiced_group.title} - Facture {other_invoice.official_number}"
                        " du {}".format(other_invoice.date.strftime("%d/%m/%Y"))
                    )
                    group = TaskLineGroup(
                        title=title,
                        description=invoiced_group.description,
                        display_details=invoiced_group.display_details,
                    )
                    current_order = 0
                    for invoiced_line in invoiced_group.lines:
                        line = invoiced_line.duplicate()
                        line.cost = -1 * line.cost
                        line.order = current_order
                        current_order += 1
                        group.lines.append(line)

                    line_groups.append(group)

            invoice.line_groups = line_groups
            # Idem pour les remises, il faut les dupliquer
            invoice.discounts = self._duplicate_estimation_discounts()
            invoice.cache_totals(self.request)
        self.request.dbsession.merge(invoice)
        self.request.dbsession.flush()
        return invoice
