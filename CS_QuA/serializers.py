from rest_framework import serializers
from .models import *


class Question_serializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class Answer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'