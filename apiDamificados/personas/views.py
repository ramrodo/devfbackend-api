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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
