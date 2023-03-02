from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(name, email, phone, prog, started):
    subject = 'Запись в Tundra School'
    if started:
        html_message = render_to_string(
            'html/mail_sign_up_started.html', {'context': 'values', 'name': name, 'program': prog}
        )
    else:
        html_message = render_to_string(
            'html/mail_sign_up.html', {'context': 'values', 'name': name, 'program': prog}
        )
    plain_message = strip_tags(html_message)
    from_email = 'no-reply@tundra-school.ru'
    to = email
    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

