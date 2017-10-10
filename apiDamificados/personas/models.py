"""Docstring public module."""
from django.db import models


SEXOS = (("M", "Mujer"), ("H", "Hombre"), ("I", "Indefinido"))
TIPOSPERSONAS = (
    ("Voluntario", "Voluntario"),
    ("Damificado", "Damificado"),
    ("Otro", "Otro"))


class Personas(models.Model):
    """Docstring class."""

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(choices=SEXOS, max_length=5)
    tipo_de_persona = models.CharField(choices=TIPOSPERSONAS, max_length=50)
