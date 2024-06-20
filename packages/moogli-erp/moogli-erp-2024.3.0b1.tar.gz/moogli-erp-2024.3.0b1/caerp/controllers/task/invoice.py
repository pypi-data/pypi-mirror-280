from typing import List
from caerp.models.task import Estimation, Invoice
from caerp.models.task.invoice import CancelInvoice


def attach_invoice_to_estimation(request, invoice: Invoice, estimation: Estimation):
    """Attach an invoice to an estimation and handle business related informations"""
    estimation.geninv = True
    invoice.estimation_id = estimation.id
    if estimation.business_id:
        business = estimation.business
        invoice.business_id = business.id
        business.status_service.update_invoicing_status(business, invoice)
        # On supprime l'affaire si nécessaire
        invoice.on_before_commit(request, "delete")
    else:
        estimation.business_id = invoice.business_id
    request.dbsession.merge(estimation)


def attach_invoices_to_estimation(
    request, estimation: Estimation, invoices: List[Invoice] = None
):
    for invoice in invoices:
        attach_invoice_to_estimation(request, invoice, estimation)
