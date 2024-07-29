from django.urls import path
from . import views

urlpatterns = [
    path("dashboard", views.dashboard, name = "dashboard"),
    path("all", views.all, name = "all"),
    path("create", views.create_an_asset, name="create"),
    path("all/<int:asset_id>", views.asset_detail, name="asset_detail"),
    path("", views.page_redirect),
    #path("<other_path>", views.throw_error)
]
