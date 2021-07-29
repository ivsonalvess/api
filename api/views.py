from rest_framework import generics, status
from api.models import PersonType, PersonMediaType, Person, PersonMedia, PersonAudit

class PersonType(generics.ListAPIView):
    queryset = PersonType.objects.all()

class PersonMediaType(generics.ListAPIView):
    queryset = PersonMediaType.objects.all()

class Person(generics.ListAPIView):
    queryset = Person.objects.all()

class PersonMedia(generics.ListAPIView):
    queryset = PersonMedia.objects.all()

class PersonAudit(generics.ListAPIView):
    queryset = PersonAudit.objects.all()
