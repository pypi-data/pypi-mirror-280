from typing import List
from sqlalchemy import func, select
from caerp.controllers.task.estimation import EstimationInvoicingController
from caerp.models.project.business import BusinessPaymentDeadline
from caerp.models.task import Task


def gen_invoice_from_payment_deadline(
    request,
    business,
    payment_deadline,
    add_estimation_details=False,
):
    controller = EstimationInvoicingController(payment_deadline.estimation, request)
    if payment_deadline.deposit:
        invoice = controller.gen_deposit_invoice(
            request.identity,
            payment_deadline.description,
            payment_deadline.amount_ttc,
            date=payment_deadline.date,
            add_estimation_details=add_estimation_details,
        )
    elif payment_deadline == business.payment_deadlines[-1]:
        return gen_sold_invoice(request, business, payment_deadline)
    else:
        invoice = controller.gen_intermediate_invoice(
            request.identity,
            payment_deadline.description,
            payment_deadline.amount_ttc,
            date=payment_deadline.date,
            add_estimation_details=add_estimation_details,
        )
    payment_deadline.invoice_id = invoice.id
    request.dbsession.merge(payment_deadline)
    return invoice


def gen_new_intermediate_invoice(request, business, add_estimation_details=False):
    """
    Generate an intermediate invoice not related to a payment deadline
    """
    controller = EstimationInvoicingController(business.estimations[-1], request)
    invoice = controller.gen_intermediate_invoice(
        request.identity,
        "Nouvelle facture",
        0,
        add_estimation_details=add_estimation_details,
    )
    return invoice


def gen_sold_invoice(request, business, payment_deadline=None):
    if payment_deadline is None:
        payment_deadline = business.payment_deadlines[-1]
    controller = EstimationInvoicingController(payment_deadline.estimation, request)
    invoice = controller.gen_sold_invoice(request.identity, date=payment_deadline.date)
    payment_deadline.invoice_id = invoice.id
    request.dbsession.merge(payment_deadline)
    return invoice


def currently_invoicing(request, business):
    query = (
        select(func.count(Task.id))
        .where(Task.business_id == business.id)
        .where(Task.status != "valid")
    )

    return request.dbsession.execute(query).scalar() != 0


def find_payment_deadline_by_id(request, business, deadline_id):
    """Return the payment deadline with the given id attached to the business"""
    return (
        request.dbsession.query(BusinessPaymentDeadline)
        .filter_by(business_id=business.id)
        .filter_by(id=deadline_id)
        .first()
    )


def get_deadlines_by_estimation(
    request, business
) -> List[List[BusinessPaymentDeadline]]:
    """
    Group a business' payment deadlines by estimation
    """
    result = {}
    for deadline in business.payment_deadlines:
        result.setdefault(deadline.estimation_id, []).append(deadline)
    return result.values()


def get_sold_deadlines(request, business) -> List[BusinessPaymentDeadline]:
    """Collect the sold payment deadlines of a business"""
    return [a[-1] for a in get_deadlines_by_estimation(request, business)]
