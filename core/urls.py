from django.urls import path

from . import views

urlpatterns = [
    path("", views.TextView.as_view(), name="index")
]