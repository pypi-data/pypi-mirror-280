"""
Timeline related panels

a Timeline is a <ul> consisting of successive <li> that will be displayed left/right
"""
import typing
import datetime
from dataclasses import dataclass
from sqlalchemy import select

from caerp.controllers.business import (
    currently_invoicing,
    get_deadlines_by_estimation,
    get_sold_deadlines,
)

from caerp.models.project.business import Business, BusinessPaymentDeadline
from caerp.models.task import Estimation, Invoice, CancelInvoice, Task
from caerp.utils.datetimes import format_date
from caerp.utils.strings import (
    format_amount,
    format_cancelinvoice_status,
    format_estimation_status,
    format_invoice_status,
)
from caerp.utils.widgets import POSTButton, Link

from caerp.views.business.routes import (
    BUSINESS_ITEM_INVOICING_ROUTE,
    BUSINESS_PAYMENT_DEADLINE_ITEM_ROUTE,
    BUSINESS_ITEM_PROGRESS_INVOICING_ROUTE,
)
from caerp.views.task.utils import task_pdf_link, get_task_url

from caerp.panels import BasePanel


@dataclass
class Action:
    title: str
    button: POSTButton
    description: typing.Optional[str] = None


def progress_invoicing_url(business, request, _query={}):
    """
    Build the progress invoicing invoicing url

    :rtype: str
    """
    return request.route_path(
        BUSINESS_ITEM_PROGRESS_INVOICING_ROUTE, id=business.id, _query=_query
    )


def _get_sort_representation(item: typing.Union[Task, BusinessPaymentDeadline]) -> list:
    """
    Build representations of the item used to sort Tasks and BusinessPaymentDeadlines
    1- by date
    2- by item type (Task > BusinessPaymentDeadline)
    3- by order (for BusinessPaymentDeadline)

    Used to sort element in the timeline
    """
    d = None
    item_type_index = 2
    if isinstance(item, Task):
        item_type_index = 0
        d = item.date
    elif isinstance(item, BusinessPaymentDeadline):
        item_type_index = 1
        if item.invoiced:
            d = item.invoice.date
            item_type_index = 0
        elif item.date and item.date != item.estimation.date:
            d = item.date
        else:
            d = datetime.date(3000, 1, item.order + 1)

    return [d.year, d.month, d.day, item_type_index]


class BusinessClassicTimelinePanel(BasePanel):
    """
    Panel rendering a timeline of a business in classic mode

    Shows :
    - Estimations
    - CancelInvoices
    - Invoices
    - BusinessPaymentDeadlines
    - Additional actions

    In the order defined through the _get_sort_representation
    """

    panel_name = "payment_deadline_timeline"
    template = "caerp:templates/panels/business/payment_deadline_timeline.mako"

    def _get_add_task_button(self, disabled=False):
        """
        Build a button to generate a new intermediary invoice
        """
        url = self.request.route_path(
            BUSINESS_ITEM_INVOICING_ROUTE,
            id=self.context.id,
            deadline_id=0,
        )
        button = POSTButton(
            url=url,
            label="Générer la facture",
            icon="file-invoice-euro",
            css="btn small icon",
            disabled=disabled,
        )
        return Action(
            title="Ajouter une facture intermédiaire",
            description=(
                "Générer une facture intermédiaire qui n'était pas prévue dans"
                " le devis initial"
            ),
            button=button,
        )

    def _get_sold_item(self, disabled):
        """
        Build a button to generate the last invoice
        """
        sold_deadline = self.context.payment_deadlines[-1]
        if not sold_deadline.invoiced or sold_deadline.invoicing:
            return sold_deadline
        else:
            # On est dans le cas où toutes les échéances ont déjà été facturées
            # mais il reste un montant à facturer
            url = self.request.route_path(
                BUSINESS_ITEM_INVOICING_ROUTE,
                id=self.context.id,
                deadline_id=sold_deadline.id,
            )
            return POSTButton(
                url=url,
                label="Générer la facture de solde",
                icon="file-invoice-euro",
                css="btn small icon",
                disabled=disabled,
            )

    def collect_items(self):
        """
        Produce a generator for item that should be displayed in the timeline
        Estimations
        Invoices
        CancelInvoices
        BusinessPaymentDeadlines
        """
        deadlines = get_deadlines_by_estimation(self.request, self.context)

        # Les Devis, les avoirs et les factures qui ne sont pas associées à
        # des échéances de facturation
        q = (
            select(Task)
            .filter(Task.business_id == self.context.id)
            .filter(
                Task.id.notin_(
                    [
                        d.invoice_id
                        for d in self.context.payment_deadlines
                        if d.invoice_id
                    ]
                )
            )
            .order_by(Task.date.desc())
        )
        tasks = self.request.dbsession.execute(q).scalars().all()

        # On ne met pas le solde dans la liste
        for estimation_deadlines in deadlines:
            tasks.extend(estimation_deadlines[:-1])

        tasks.sort(key=_get_sort_representation)

        # On affiche un bouton pour rajouter une facture intermédiaire :
        # Si l'affaire n'est pas entièrement facturée
        # Si on a fait toutes les échéances de paiement sauf le solde
        if not self.context.invoiced:
            # Si on a une facture en cours, on affiche le bouton inactif
            disabled = currently_invoicing(self.request, self.context)
            # Il ne reste plus que le solde
            if (
                len(
                    [
                        deadline.id
                        for deadline in self.context.payment_deadlines
                        if not deadline.invoice_id
                    ]
                )
                == 1
            ):
                tasks.append(self._get_add_task_button(disabled))
            tasks.append(self._get_sold_item(disabled))
        else:
            # On ne met pas le solde dans la liste
            for estimation_deadlines in deadlines:
                tasks.append(estimation_deadlines[-1])

        return tasks

    def __call__(self):
        return {
            "to_invoice": self.context.amount_to_invoice("ttc"),
            "foreseen_to_invoice": self.context.amount_foreseen_to_invoice(),
            "items": self.collect_items(),
        }


class BusinessProgressInvoicingTimeLinePanel(BasePanel):
    """Panel rendering a timeline of a business in classic mode"""

    panel_name = "progress_invoicing_timeline"
    template = "caerp:templates/panels/business/progress_invoicing_timeline.mako"

    def collect_items(self):
        q = (
            select(Task)
            .filter(Task.business_id == self.context.id)
            .order_by(Task.date.desc())
        )

        tasks = self.request.dbsession.execute(q).scalars().all()

        if not self.context.to_invoice() == 0:
            invoicing = currently_invoicing(self.request, self.context)
            tasks.append(
                POSTButton(
                    url=progress_invoicing_url(self.context, self.request),
                    label="Générer une nouvelle facture de situation",
                    title="Facture sur le pourcentage d'avancement de l'affaire",
                    icon="file-invoice-euro",
                    css="btn small icon",
                    disabled=invoicing,
                )
            )
            tasks.append(
                POSTButton(
                    url=progress_invoicing_url(
                        self.context,
                        self.request,
                        _query={"action": "sold"},
                    ),
                    label="Générer la facture de solde",
                    title="Facturer le solde de cette affaire",
                    icon="file-invoice-euro",
                    css="btn small icon",
                    disabled=invoicing,
                )
            )
        return tasks

    def __call__(self):
        return {
            "to_invoice": self.context.amount_to_invoice("ttc"),
            "items": self.collect_items(),
        }


class BusinessPaymentDeadlineTimelinePanelItem(BasePanel):
    """Render a Business payment deadline timeline item"""

    template = (
        "caerp:templates/panels/business/business_payment_deadline_timeline_item.mako"
    )

    def _get_title(self):
        return f"Échéance : {self.context.description}"

    def _get_description(self):
        if self.context.invoice:
            date_str = format_date(self.context.invoice.date)
            amount_ttc = format_amount(self.context.invoice.total(), precision=5)
            amount_ht = format_amount(self.context.invoice.total_ht(), precision=5)
            status_str = format_invoice_status(self.context.invoice, full=True)
            if self.context.invoiced:
                return (
                    f"Facturée le {date_str} : {amount_ttc}&nbsp;€&nbsp;TTC "
                    f"({amount_ht}&nbsp;€&nbsp;HT)<br />"
                    f"{status_str}"
                )
            else:
                return (
                    f"Facture en cours d'édition le {date_str} : "
                    f"{amount_ttc}&nbsp;€&nbsp;TTC "
                    f"({amount_ht}&nbsp;€&nbsp;HT)<br />"
                    f"{status_str}"
                )
        else:
            amount_ttc = format_amount(self.context.amount_ttc, precision=5)
            amount_ht = format_amount(self.context.amount_ht, precision=5)
            if self.context.date:
                date_str = format_date(self.context.date)
                return (
                    f"Facturation prévue initialement le {date_str} : {amount_ttc}&nbsp;€&nbsp;TTC "
                    f"({amount_ht}&nbsp;€&nbsp;HT)"
                )
            else:
                return (
                    f"Facturation prévue initialement : {amount_ttc}&nbsp;€&nbsp;TTC "
                    f"({amount_ht}&nbsp;€&nbsp;HT)"
                )

    def _get_css_data(self, previous_deadline):
        status_css = "draft"
        icon = "clock"
        business_has_a_waiting_invoice = currently_invoicing(
            self.request, self.context.business
        )

        if self.context.invoiced:
            icon = "euro-sign"
            time_css = "past"
            status_css = "valid"

        elif self.context.invoicing():
            icon = "euro-sign"
            time_css = "current"
            status_css = "caution"
        elif (
            previous_deadline is None
            or (previous_deadline and previous_deadline.invoiced)
        ) and not business_has_a_waiting_invoice:
            time_css = "current"
            status_css = "caution"
        elif (
            self.context in get_sold_deadlines(self.request, self.context.business)
            and not business_has_a_waiting_invoice
        ):
            time_css = "current"
            status_css = "caution"

        else:
            time_css = "future"

        return dict(
            status_css=status_css,
            time_css=time_css,
            icon=icon,
            current=time_css == "current",
        )

    def _get_more_links(self):
        if self.request.has_permission("edit.business_payment_deadline", self.context):
            yield Link(
                self.request.route_path(
                    BUSINESS_PAYMENT_DEADLINE_ITEM_ROUTE,
                    id=self.context.id,
                    _query={"action": "edit"},
                ),
                label="",
                icon="pen",
                css="btn icon only unstyled",
                popup=True,
            )

    def _get_main_links(self, business, current):

        if self.context.invoicing():
            yield Link(
                url=get_task_url(self.request, self.context.invoice),
                label="Voir la facture",
                icon="file-invoice-euro",
                css="btn small icon",
            )
        elif self.context.invoiced:
            yield task_pdf_link(
                self.request,
                task=self.context.invoice,
                link_options={"css": "btn small icon", "label": "Voir le PDF"},
            )

            yield Link(
                get_task_url(self.request, self.context.invoice),
                label="Voir la facture",
                icon="eye",
                css="btn small icon",
            )
        elif not business.closed and current:
            url = self.request.route_path(
                BUSINESS_ITEM_INVOICING_ROUTE,
                id=business.id,
                deadline_id=self.context.id,
            )
            yield POSTButton(
                url=url,
                label="Générer la facture",
                icon="file-invoice-euro",
                css="btn small icon",
            )

    def __call__(self, previous=None, business=None, **options):
        css_data = self._get_css_data(previous)
        current = css_data["current"]
        return dict(
            title=self._get_title(),
            deadline=self.context,
            description=self._get_description(),
            main_links=list(self._get_main_links(business, current)),
            more_links=list(self._get_more_links()),
            **css_data,
        )


class BaseTaskTimelinePanelItem(BasePanel):
    template = "caerp:templates/panels/business/task_timeline_item.mako"

    def _get_title(self):
        return self.context.name

    def _get_description(self):
        return ""

    def _get_date_string(self):
        return self.context.date.strftime("%d/%m/%Y")

    def _get_main_links(self):
        yield task_pdf_link(
            self.request,
            task=self.context,
            link_options={"css": "btn small icon", "label": "Voir le PDF"},
        )
        yield Link(
            get_task_url(self.request, self.context),
            label="Voir le document",
            icon="eye",
            css="btn small icon",
        )

    def _get_status_css_data(self):
        result = {}
        if self.context.status == "draft":
            result["status_css"] = "draft"
            result["icon"] = "pen"

        elif self.context.status == "wait":
            result["status_css"] = "caution"
            result["icon"] = "clock"

        elif self.context.status == "invalid":
            result["status_css"] = "danger"
            result["icon"] = "times"
        else:
            result["status_css"] = "success"
            result["icon"] = "check"
        return result

    def _get_css_data(self):
        return self._get_status_css_data()

    def __call__(self, previous=None, business=None, **options):
        css_data = self._get_css_data()
        return dict(
            task=self.context,
            title=self._get_title(),
            date_string=self._get_date_string(),
            main_links=list(self._get_main_links()),
            description=self._get_description(),
            **css_data,
        )


class EstimationTimelinePanelItem(BaseTaskTimelinePanelItem):
    def _get_title(self):
        prefix = ""
        if "devis" not in self.context.name.lower():
            prefix = "Devis : "
        return f"{prefix}{self.context.name}"

    def _get_description(self):
        return format_estimation_status(self.context, full=True)

    def _get_date_string(self):
        result = super()._get_date_string()
        return f"Devis daté du {result}"

    def _get_css_data(self):
        result = self._get_status_css_data()
        if self.context.status == "valid":
            if self.context.signed_status == "aborted":
                result["status_css"] = "draft"
                result["icon"] = "times"
            elif self.context.signed_status == "signed" or self.context.geninv:
                result["status_css"] = "valid"
                if self.context.geninv:
                    result["icon"] = "euro-sign"
                else:
                    result["icon"] = "check"
            else:
                result["status_css"] = "valid"
                result["icon"] = "clock"

        return result


class InvoiceTimelinePanelItem(BaseTaskTimelinePanelItem):
    def _get_title(self):
        prefix = ""
        if "facture" not in self.context.name.lower():
            prefix = "Facture : "

        return f"{prefix}{self.context.name}"

    def _get_description(self):
        return format_invoice_status(self.context, full=True)

    def _get_date_string(self):
        result = super()._get_date_string()
        return f"Facturé le {result}"

    def _get_css_data(
        self,
    ):
        result = self._get_status_css_data()

        if self.context.status == "valid":
            if self.context.paid_status == "resulted":
                result["icon"] = "euro-sign"
                return result
            elif self.context.paid_status == "paid":
                result["icon"] = "euro-slash"
            else:
                result["icon"] = "check"
        if self.context.cancelinvoices:
            result["status_css"] = "draft"
        return result


class CancelInvoiceTimelinePanelItem(BaseTaskTimelinePanelItem):
    def _get_title(self):
        prefix = ""
        if "avoir" not in self.context.name.lower():
            prefix = "Avoir : "

        return f"{prefix}{self.context.name}"

    def _get_description(self):
        return format_cancelinvoice_status(self.context, full=True)

    def _get_date_string(self):
        result = super()._get_date_string()
        return f"Avoir daté du {result}"


class ActionTimeLineItemPanel(BasePanel):
    """Render an Action as a timeline item"""

    template = "caerp:templates/panels/business/button_timeline_item.mako"

    def __call__(self, previous=None, business=None, **options):
        status_css = "caution"
        time_css = "current"
        if self.context.button.disabled:
            status_css = "draft"
            time_css = "future"
        return {
            "title": self.context.title,
            "description": self.context.description,
            "button": self.context.button,
            "status_css": status_css,
            "time_css": time_css,
        }


def includeme(config):
    for panel in (
        BusinessClassicTimelinePanel,
        BusinessProgressInvoicingTimeLinePanel,
    ):
        config.add_panel(
            panel,
            name=panel.panel_name,
            context=Business,
            renderer=panel.template,
        )

    for panel, context in (
        (BusinessPaymentDeadlineTimelinePanelItem, BusinessPaymentDeadline),
        (EstimationTimelinePanelItem, Estimation),
        (InvoiceTimelinePanelItem, Invoice),
        (CancelInvoiceTimelinePanelItem, CancelInvoice),
        (ActionTimeLineItemPanel, Action),
    ):
        config.add_panel(
            panel,
            name="timeline_item",
            context=context,
            renderer=panel.template,
        )
