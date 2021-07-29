from django.urls import path
from api import views

api_urls = [
    path('person-type', views.PersonType.as_view()),
    path("person-media-type", views.PersonMediaType.as_view()),
    path("persob", views.Person.as_view()),
    path("person-media", views.PersonMedia.as_view()),
    path("person-audit", views.PersonAudit.as_view()),
]