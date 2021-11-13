from django.urls import path
from message import views

urlpatterns = [
    path("<name>/<age>", views.message, name="message"),
]