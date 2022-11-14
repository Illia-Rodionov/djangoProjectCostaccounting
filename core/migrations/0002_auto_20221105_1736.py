from core.models import Category
from django.db import migrations


def creating_default_categories_consumption(apps, schema_editor):
    for consumption_category in Category.DEFAULT_USER_CATEGORIES_CONSUMPTION:
        Category.objects.get_or_create(name=consumption_category, transaction_type=2)


def creating_default_categories_income(apps, schema_editor):
    for income_category in Category.DEFAULT_USER_CATEGORIES_INCOME:
        Category.objects.get_or_create(name=income_category, transaction_type=1)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [migrations.RunPython(creating_default_categories_consumption),
                  migrations.RunPython(creating_default_categories_income)]
