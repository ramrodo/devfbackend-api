"""Docstring."""
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Personas
from .serializers import PeopleGetName, PersonasCreationSerializer, PersonasSerializer


class PersonasApi(APIView):
    """Clase."""

    def get(self, request):
        """Get REST."""
        people = Personas.objects.all()
        # Many: Query DB
        # serializer = PeopleGetName(people, many=True)
        serializer = PersonasSerializer(people, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Method POST implemented."""
        # serializer = PersonasCreationSerializer(data=request.data)
        serializer = PersonasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self._sendPushNotification("Nueva Persona Creada", "dMQzfx5mn7k:APA91bHbFfdCzV6BRzVIU0h8GZgdHczJyUU_UADQ4_wcil0uq_SuNxLXB0LAlwewUrB60BdHBQMHBN0-rdRdIVjqSU8OoogrbCDmw-fm90qQePkw3G_lDrFzMZhH4F1T9Wu_xwC0bK4N")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _sendPushNotification(self, msg, token):
        baseUrl = "https://fcm.googleapis.com/fcm/send"
        headers = {"Authorization":"key=AIzaSyB0k006LxEMxjpcL1bgz6CkAtEhX2UjQdY", "Content-Type":"application/json"}
        data = { "notification": {"title": "Sadot EscoBBBBBBBBBar","body": "5 to 1","icon": "firebase-logo.png","click_action": "http://localhost:8081"},"to" : token}
        data = json.dumps(data)
        pushNotificacionJson = requests.post(baseUrl, headers=headers, data=data)
        if pushNotificacionJson.status_code == 200 and "error" not in pushNotificacionJson['results'][0]:
            return True
        else:
            return False


class PersonaApi(APIView):

    def _getPersona(self, pk):
        try:
            return Personas.objects.get(pk=pk)
        except Personas.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        persona = self._getPersona(pk)
        serializer = PersonasSerializer(persona)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        persona = self._getPersona(pk)
        serializers = PersonasSerializer(persona, request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response(serializers, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        persona = self._getPersona(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
