from celery import shared_task

from django.core.mail import send_mail

from .models import Order

from datetime import timedelta

from django.utils import timezone






@shared_task
def order_created(order_id):

    order = Order.objects.get(id=order_id)

    subject = f"Заказ №{order.id}"

    message =  f"Ваш заказ №{order.id} успешно оплачен"

    mail_sent = send_mail(
        subject,
        message,
        'kaznacheev1300@mail.ru',
        [order.user.email]
    )


@shared_task
def delete_unpaid_orders():

    time_threshold = timezone.now() - timedelta(minutes=1)

    Order.objects.filter(paid=False, created__lt=time_threshold).delete()






