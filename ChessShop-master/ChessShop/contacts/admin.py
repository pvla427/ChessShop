from django.contrib import admin
from .models import ContactEntry, Location 

admin.site.register([ContactEntry, Location])

# Register your models here.
