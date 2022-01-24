from django.db import models
from django.db.models import fields
from rest_framework import serializers
from CS_Back.models import *
class Notes_Serailzer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
