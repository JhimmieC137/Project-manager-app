import datetime
from typing import Any
from django.db import models
from datetime import timezone
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string



# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Project name', max_length=100, null=True, blank=False)
    due_in = models.CharField("Due date", max_length=50)
    tasks_completed = models.IntegerField('Number of completed tasks')
    tasks = models.IntegerField(null=True)
    # status
    # countries = models.CharField('Countries applicable for this form', max_length=2000, null=False, blank=False)
    # img = models.ImageField(blank=False, null=False, upload_to= 'src.agency.form_images')
    # document = models.FileField(blank=False, null=True, upload_to= 'src.agency.forms')
    
    def __str__(self):
        return f'{self.name}'
    