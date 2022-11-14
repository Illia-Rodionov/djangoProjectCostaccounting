from django.urls import path, include
from rest_framework import routers

from core.views import UserViewsSet, TransactionViewsSet, CategoryViewsSet


app_name = "core"

router = routers.SimpleRouter()
router.register(r"user", UserViewsSet, basename='user')
router.register(r"transaction", TransactionViewsSet, basename='transaction')
router.register(r"category", CategoryViewsSet, basename='category')

urlpatterns = [
    path("", include(router.urls)),
]