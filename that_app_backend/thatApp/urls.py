from django.urls import path

from .views import PingPong

urlpatterns = [
    path("", PingPong, name="testing")
]