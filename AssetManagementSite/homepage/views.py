from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string


def main_page(request):
    response_data = render_to_string("homepage/home.html")
    return HttpResponse(response_data)


