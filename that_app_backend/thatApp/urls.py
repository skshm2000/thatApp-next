from django.urls import path

from .views import PingPong, CreateUser

urlpatterns = [
    path("", PingPong, name="sanity"),
    path("create", CreateUser, name="crete_user"),
]
