from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Hello, this is the home page")
