from datetime import date, timedelta
from django.db.models import Sum
from config.celery import app
from core.models import Category, User
from core.send_mail import mail_send


def get_statistic():
    """The function gets all users.

    user_transaction - Get all user transactions.
    user_email - Get user email.
    user_sum - Get the sum of all transactions by filtering them by date for the last day, by category CONSUMPTION
    email_text - The text of the mail message that is sent to the mail.
    mail_send - Function that sends an email to user_email"""
    users = User.objects.all()
    for user in users:
        user_transaction = user.transaction_set.all()
        user_email = user.email
        user_sum = user_transaction.filter(date=date.today() - timedelta(days=1),
                                           category__transaction_type=Category.CONSUMPTION).aggregate(Sum('sum'))

        email_text = f"Statistics for the user - {user_email}, Amount of expenses for yesterday: " \
                     f"{user_sum['sum__sum']}$."

        mail_send(user_email, email_text)


@app.task
def main():
    get_statistic()


if __name__ == "main":
    main()
