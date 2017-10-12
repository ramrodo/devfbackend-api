"""Docstring."""
from rest_framework import serializers

from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    """Docstring."""

    class Meta:
        """Tal y como lo mapeamos en el modelo lo pondra en"""

        model = Users
        fields = ['id', 'email', 'password']

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)
