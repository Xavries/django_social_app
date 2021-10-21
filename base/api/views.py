from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializer import Room_serializer
from base.api import serializer

@api_view(['GET'])
def  get_routes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id1'
    ]
    return Response(routes)

@api_view(['GET'])
def get_rooms(request):
    rooms = Room.objects.all()
    serializer = Room_serializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_room(request, pk):
    room = Room.objects.get(id=pk)
    serializer = Room_serializer(room, many=False)
    return Response(serializer.data)