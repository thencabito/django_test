from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("Oscar", views.Oscar, name="Oscar"),
	path("<str:name>", views.greet, name="greet")
]