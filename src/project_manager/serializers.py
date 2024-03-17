from rest_framework import serializers
from django.template.loader import  get_template, select_template, render_to_string
from django.core.mail import EmailMessage,  EmailMultiAlternatives
import datetime

from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'