from django.urls import path
from . import views

urlpatterns = [
    path("dashboard", views.dashboard),
    path("all", views.all),
    path("create", views.create_an_asset),
]
