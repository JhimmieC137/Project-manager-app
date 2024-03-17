from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Project

# Register your models here.
admin.site.register(Project)