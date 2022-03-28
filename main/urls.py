from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("LOOKATTHIS", views.shop),
    path("C0N6RATULAT10N5", views.access_admin),
    path("4dm1n_4cc355", views.final),
]
