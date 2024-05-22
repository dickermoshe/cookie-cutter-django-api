from accounts.models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:  # type: ignore
        model = CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "is_staff",
            "email",
            "is_active",
            "date_joined",
            "last_login",
        ]
