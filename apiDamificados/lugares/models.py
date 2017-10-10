"""Docstring public module."""
from django.db import models


class Lugares(models.Model):
    """Docstring."""

    nombre = models.CharField(max_length=180)
    calle = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()
