from django.shortcuts import render, redirect
from django.http import Http404
from django.db.models import Sum
from .models import Asset

def dashboard(request):
    assets = Asset.objects.all()
    asset_count = assets.count()
    total_purchase_cost = assets.aggregate(Sum('purchase_cost'))['purchase_cost__sum'] or 0
    return render(request, "assetmanager/dashboard.html", {"assets": assets, "asset_count": asset_count, "total_purchase_cost": total_purchase_cost})

def all(request):
    assets = Asset.objects.all()
    return render(request, "assetmanager/all.html", {"assets": assets})
    
def create_an_asset(request):
    return render(request, "assetmanager/create.html")

def page_redirect(request):
    return redirect("dashboard")

def throw_error(request, other_path):
    raise Http404()

def asset_detail(request, asset_id):
    asset = Asset.objects.get(asset_tag= asset_id)
    return render(request, "assetmanager/asset_details.html", {"asset": asset})