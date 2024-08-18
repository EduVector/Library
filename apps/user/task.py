import smtplib
from django.core.mail import EmailMessage

from .models import User
from celery import shared_task


@shared_task
def send_email(subject, message, to_email):
    print(f"Sending email --------- {to_email}, ---------- {subject}, ---------- {message}")
    email = EmailMessage(to=[to_email], subject=subject, body=message)
    email.send()
