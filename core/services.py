from django_filters import rest_framework as filters
from core.models import Transaction


class TransactionFilter(filters.FilterSet):
    sum = filters.NumberFilter(field_name="sum")
    date = filters.DateFilter(field_name="date")
    time = filters.TimeFilter(field_name="time")

    class Meta:
        model = Transaction
        fields = ("sum", "date", "time")

