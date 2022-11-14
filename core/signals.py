from django.dispatch import receiver
from django.db.models.signals import pre_save
from rest_framework.exceptions import APIException

from core.models import Transaction, Category


@receiver(pre_save, sender=Transaction)
def transaction_pre_save(instance: Transaction, **kwargs):
    """ When creating and updating a transaction, a signal is triggered,
        replenishment and reduction of balance.

        get_user_balance - Getting a user's balance,
        get_transaction_sum - Getting the transaction amount,
        get_existing_transaction - Getting an existing transaction,
        get_transaction_difference - Getting the difference between new and existing transactions."""
    if instance.pk is None:
        get_user_balance = instance.user.balance
        get_transaction_sum = instance.sum
        if instance.category.transaction_type == Category.CONSUMPTION:
            if get_user_balance < get_transaction_sum:
                raise APIException("Not enough money!")
            else:
                result = get_user_balance - get_transaction_sum
                instance.user.balance = result
                instance.user.save()
        else:
            result = get_transaction_sum + get_user_balance
            instance.user.balance = result
            instance.user.save()
    else:
        get_existing_transaction = Transaction.objects.get(pk=instance.pk)
        get_transaction_difference = instance.sum - get_existing_transaction.sum
        if get_existing_transaction.sum < instance.sum:
            result = get_transaction_difference + instance.user.balance
            instance.user.balance = result
            instance.user.save()
        else:
            result = instance.user.balance + get_transaction_difference
            if result < 0:
                raise APIException("Insufficient funds, transaction not updated")
            else:
                instance.user.balance = result
                instance.user.save()




