"""Docstring."""
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Lugares
from .serializers import LugaresSerializer


class LugaresApi(APIView):
    """Clase."""

    def get(self, request):
        """Get REST."""
        lugares = Lugares.objects.all()
        serializer = LugaresSerializer(lugares, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Method POST implemented."""
        serializer = LugaresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
