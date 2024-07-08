from django.shortcuts import render


def dashboard(request):
    return render(request, "assetmanager/dashboard.html")

def all(request):
    return render(request, "assetmanager/all.html")
    
def create_an_asset(request):
    return render(request, "assetmanager/create.html")
