from rest_framework import serializers
from core.models import User, Transaction, Category


class UserCreateSerializer(serializers.ModelSerializer):
    """CreateSerializer"""
    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserDetailUpdateDeleteSerializer(serializers.ModelSerializer):
    """DetailDeleteUpdateSerializer"""
    created_at = serializers.CharField(read_only=True)
    balance = serializers.FloatField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "created_at", "password", "balance")


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    """CategoryCreateSerializer"""
    class Meta:
        model = Category
        fields = ("name", "transaction_type", "user")


class TransactionCreateSerializer(serializers.ModelSerializer):
    """TransactionSerializer"""
    user = serializers.SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        model = Transaction
        fields = ("id", "sum", "date", "time", "category",
                  "organization", "description", "user")

    def create(self, validated_data):
        """When creating a transaction user == user.request"""
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class TransactionUpdateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())
    """TransactionUpdateSerializer"""
    class Meta:
        model = Transaction
        fields = ("id", "sum", "category", "organization", "description", "date", "time")
