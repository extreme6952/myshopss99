from django.template.loader import render_to_string

from io import BytesIO

from orders.models import Order

from django.core.mail import EmailMessage

from celery import shared_task

from django.conf import settings

from django.contrib.auth.models import User

import weasyprint



@shared_task
def payment_send_pdf_file(order_id):

    order = Order.objects.get(id=order_id)

    subject = f"Ваш чек об оплате заказа №{order.id}"

    message = f"Пожалуйста убедитесь,что все товары соответсвуют  вашему заказу"

    email = EmailMessage(subject,
                         message,
                         'kaznacheev1300@mail.ru',
                         [order.user.email])

    out = BytesIO()

    html = render_to_string('payment/pdf_file_payment/pdf.html',
                                {'order':order})
    
    stylesheets = [weasyprint.CSS(settings.STATICFILES_DIRS[0] / 'css/pdf.css')]

    weasyprint.HTML(string=html).write_pdf(out,
                                           stylesheets=stylesheets)
    
    email.attach(f'заказ_{order.id}',
                 out.getvalue(),
                 'application/pdf')
    
    email.send()
    
