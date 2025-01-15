from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services.account_service import AccountService


@api_view(["GET"])
def PingPong(request):
    return Response({"message": "Hello world, PONG!", "status": "success"})


@api_view(["POST"])
def CreateUser(request):
    data = request.data
    instance = AccountService()
    creation = instance.create_new_account(data=data)

    if creation["success"] == True:
        return Response(
            {"message": "User created successfully", "data": creation["data"]},
            status=status.HTTP_201_CREATED,
        )
    else:
        return Response(
            {"message": "User creation failed", "data": creation["data"]},
            status=status.HTTP_400_BAD_REQUEST,
        )
