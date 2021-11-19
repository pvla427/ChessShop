from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<b>text/b>')

def about(request):
    return HttpResponse('<i>text</i>')


# Create your views here.
