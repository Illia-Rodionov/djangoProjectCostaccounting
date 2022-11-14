from core.models import User, Transaction, Category
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from core.serializers import UserCreateSerializer, UserDetailUpdateDeleteSerializer, TransactionCreateSerializer,\
    TransactionUpdateSerializer, CategorySerializer
from core.services import TransactionFilter


class UserViewsSet(viewsets.ModelViewSet):
    """UserViewsSet"""
    queryset = User.objects.all()
    serializer_class = UserDetailUpdateDeleteSerializer
    permission_classes = ()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        else:
            return super().get_serializer_class()

    def get_queryset(self):
        """Return an object for the current authenticated user only"""
        return self.queryset.filter(email=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class TransactionViewsSet(viewsets.ModelViewSet):
    """TransactionViewsSet"""
    queryset = Transaction.objects.all()
    serializer_class = TransactionUpdateSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = TransactionFilter
    ordering_fields = ["sum", "date", "time"]

    def get_serializer_class(self):
        if self.action == "create":
            return TransactionCreateSerializer
        else:
            return super().get_serializer_class()

    def get_queryset(self):
        """Return an object for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user)


class CategoryViewsSet(viewsets.ModelViewSet):
    """CategoryViewsSet"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




