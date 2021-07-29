from django.db import models

class PersonType:
    id = models.AutoField(max_length=32, primary_key=True) 

class PersonMediaType:
    name = models.CharField(max_length=32, null=False)

class Person(models.Model):
    name = models.CharField(max_length=32, null=False)
    type = models.ForeignKey(PersonType, related_name='person_type', on_delete=models.CASCADE, default=None)
    cpf = models.CharField(max_length=14, null=False)
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=32, null=False)
    last_update = models.DateTimeField(auto_now=True)

class PersonMedia:
    person_id = models.ForeignKey(Person, related_name='person', on_delete=models.CASCADE, default=None)
    object_media = models.TextField(null=True, blank=True)

class PersonAudit:
    person_id = models.ForeignKey(Person, related_name='person', on_delete=models.CASCADE, default=None)
    type = models.IntegerField(default=0, null=False)
    cpf_new = models.CharField(max_length=14, null=False)
    cpf_old = models.CharField(max_length=14)
    last_update = models.DateTimeField(auto_now=True)
