"""Docstring."""
from rest_framework import serializers

from .models import Personas


SEXOS = (("M", "Mujer"), ("H", "Hombre"), ("I", "Indefinido"))
TIPOSPERSONAS = (
    ("Voluntario", "Voluntario"),
    ("Damificado", "Damificado"),
    ("Otro", "Otro"))


def validar_edad(edad):
    """Docstring."""
    if edad < 100:
        pass
    else:
        raise serializers.ValidationError("No hay nadie mayor a 100 años")


class PeopleGetName(serializers.Serializer):
    """Get."""

    nombre = serializers.CharField()


class PersonasCreationSerializer(serializers.Serializer):
    """Lógica de negocios. Creación."""

    nombre = serializers.CharField(max_length=50)
    edad = serializers.IntegerField(validators=[validar_edad])
    sexo = serializers.CharField(max_length=5)
    tipo_de_persona = serializers.CharField(max_length=50)

    def create(self, validated_data):
        """Because sserializers.Serializer is derived from BaseSerializer."""
        return Personas.objects.create(**validated_data)


class PersonasSerializer(serializers.ModelSerializer):
    """Docstring."""

    class Meta:
        """Docstring."""

        model = Personas
        fields = ["nombre", "edad", "sexo", "tipo_de_persona"]


class PersonasModifierSerializer(serializers.Serializer):
    """Lógica de negocios. Modificar."""

    tipo_de_persona = serializers.CharField(max_length=50)
