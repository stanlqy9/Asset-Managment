from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseNotFound, Http404


def dashboard(request):
    return render(request, "assetmanager/dashboard.html")

def all(request):
    return render(request, "assetmanager/all.html")
    
def create_an_asset(request):
    return render(request, "assetmanager/create.html")

def page_redirect(request):
    return redirect("dashboard")

def throw_error(request, other_path):
    raise Http404()

