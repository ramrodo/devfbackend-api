from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Personas
from .serializers import *
import json

class PersonasTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.primer_persona = Personas.objects.create(nombre="Rodo", edad=24, sexo="H", tipo_de_persona="Voluntario")
        self.segunda_persona = Personas.objects.create(nombre="Laura", edad=24, sexo="M", tipo_de_persona="Damificado")
        self.persona_correcta_json = {
            "nombre": "Jessica",
            "edad": 25,
            "sexo": "M",
            "tipo_de_persona": "Damificado"
        }
        self.persona_invalida_json = {
            "nombre": "Jessica",
            "edad": 25,
            "sexo": "666",
            "tipo_de_persona": "Damificado"
        }

    def test_get_all_personas(self):
        response = self.client.get(reverse("personas_endpoint"))
        personas = Personas.objects.all()
        serializer = PersonasSerializer(personas, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_get_persona(self):
        response = self.client.get(reverse("persona_endpoint", kwargs={"pk": self.primer_persona.id}))
        persona = Personas.objects.get(pk=self.primer_persona.id)
        serializer = PersonasSerializer(persona)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)

    def test_post_persona(self):
        response = self.client.post(
            reverse("personas_endpoint"),
            data=json.dumps(self.persona_correcta_json),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)