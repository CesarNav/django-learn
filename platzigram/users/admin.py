""" User admin classes """
# Django
from django.contrib import admin

# Local models
from users.models import Profile

# Register your models here.
admin.site.register(Profile)