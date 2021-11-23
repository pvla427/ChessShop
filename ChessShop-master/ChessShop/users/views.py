from django.shortcuts import render
from . import models

# Create your views here.
def get_account(request,id):
    user = models.UserAccount.objects.get(id = id)

def register(request):
    if (request.method == "POST"):
        user = models.UserAccount()
        user.save()
    else:
         pass
    