"""Docstring."""
from rest_framework import serializers

from .models import Lugares


class LugaresSerializer(serializers.ModelSerializer):
    """Docstring."""

    class Meta:
        """Docstring."""

        model = Lugares
        fields = ["nombre", "calle", "colonia", "codigo_postal"]
