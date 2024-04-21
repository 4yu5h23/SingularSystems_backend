from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['POST'])

def getinput(self, request):
    data = request.data
    print(data)
    return Response(data)

