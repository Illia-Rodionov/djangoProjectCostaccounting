from config import settings
from django.core.mail import send_mail

gmail_user = settings.EMAIL_HOST_USER
gmail_password = settings.EMAIL_HOST_PASSWORD


def mail_send(user_email, email_text):
    send_mail(subject=email_text,
              message=email_text,
              from_email=gmail_user,
              recipient_list=[user_email],
              fail_silently=False,
              auth_user=gmail_user,
              auth_password=gmail_password

    )
