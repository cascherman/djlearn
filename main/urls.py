from django.urls import path
from . import views

urlpatterns = [
    path("", views.body, name="main-body"),
]