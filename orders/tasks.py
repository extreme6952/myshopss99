from celery import shared_task

from django.core.mail import send_mail

from .models import Order






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