from django.shortcuts import render
from . import models
# Create your views here.

def view_contact(request):
    contact = models.ContactEntry.objects.get()
    location = models.Location.objects.get()

def new_contact(request):
    pass