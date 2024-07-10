from django.urls import path
from . import views

urlpatterns = [
    # if empty url -- root, go to home section
    path("", views.home, name = "home"),
]