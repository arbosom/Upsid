from django.shortcuts import render
from django.http import HttpResponse

def accueil_site (request) :
    return HttpResponse("Notre futur site")
