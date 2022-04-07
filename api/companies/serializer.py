from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelField):
    class Meta:
        model = Company
        fields=["id","name","status","application_link","last_update","notes"]