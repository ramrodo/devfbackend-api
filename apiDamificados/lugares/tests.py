from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Lugares
from .serializers import *
import json

class LugaresTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.primer_lugar = Lugares.objects.create(
            nombre="Escuela",
            codigo_postal="54400",
            calle="Calle 8",
            colonia="Mount")
        self.segundo_lugar = Lugares.objects.create(
            nombre="Estadio",
            codigo_postal="72310",
            calle="Prudencia",
            colonia="Nueva")

        self.lugar_correcto_json = {
            "nombre": "Hospital",
            "codigo_postal": "54470",
            "calle": "Condesa",
            "colonia": "Villahermosa"
        }
        self.lugar_invalido_json = {
            "nombre": "Hospital",
            "codigo_postal": 00000,
            "calle": "Condesa",
            "colonia": "Villahermosa"
        }

    def test_get_all_lugares(self):
        response = self.client.get(reverse("lugares_endpoint"))
        lugares = Lugares.objects.all()
        serializer = LugaresSerializer(lugares, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_post_lugar(self):
        response = self.client.post(
            reverse("lugares_endpoint"),
            data=json.dumps(self.lugar_correcto_json),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)

