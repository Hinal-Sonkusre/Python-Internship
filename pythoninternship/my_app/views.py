from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepageview(request):
    return HttpResponse("<b><h1>Welcome to Django!!</h1></b>")


def aboutpageview(request):
    return HttpResponse("About us page..")


def contactpageview(request):
    return HttpResponse("Contact us page..")
