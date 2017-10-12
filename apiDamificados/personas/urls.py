"""Docstring public method."""
from django.conf.urls import url
from .views import PersonasApi, PersonaApi

urlpatterns = [
    url(r'^$', PersonasApi.as_view()),
    url(r'(?P<pk>[0-9]+)/$',PersonaApi.as_view())
]
