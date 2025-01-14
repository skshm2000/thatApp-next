from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def PingPong(request):
    return Response({
        "message": "Hello world, PONG!",
        "status": "success"
    })