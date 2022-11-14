from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from core.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    """User model"""
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=100, db_index=True, unique=True, null=False, blank=False)
    balance = models.FloatField(default=0.0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"{self.email}"


class Transaction(models.Model):
    """Transaction model"""
    sum = models.FloatField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    organization = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.sum, self.category,  self.user,}"


class Category(models.Model):
    """Category Model"""
    INCOME = 1
    CONSUMPTION = 2

    TRANSACTION_TYPE = ((INCOME, "Income"),
                        (CONSUMPTION, "Consumption")
                        )

    DEFAULT_USER_CATEGORIES_INCOME = ["Зарплата"]

    DEFAULT_USER_CATEGORIES_CONSUMPTION = ["Забота о себе", "Здоровье и фитнес", "Кафе и рестораны", "Машина",
                                            "Образование", "Отдых и развлечения", "Платежи, комиссии",
                                           "Покупки: одежда, техника", "Продукты", "Проезд"]

    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTION_TYPE)

    def __str__(self) -> str:
        return self.name
