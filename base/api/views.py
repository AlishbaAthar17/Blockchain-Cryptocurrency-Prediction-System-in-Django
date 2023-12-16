#we want to respond with some json data when someone goes to our url
# from django.http import JsonResponse
#Javascrip object notation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import SerializeRoom


@api_view(['GET'])
def getRoutes(request): #shows us all the routes in our api
    #The routes will be two GET methods
    routes = [
        'GET /api',
        'GET /api/rooms', #will give json array of objects of all the rooms in our DB
        'GET /api/rooms/:id' #will get us a single object and info of a single room
    ]

    # return JsonResponse(routes, safe=False) #safe allows us to turn the list of routes into a json list
    return Response(routes) #safe allows us to turn the list of routes into a json list

#Response cannot return python objects as JSON so for this we will use serializers

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = SerializeRoom(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSingleRoom(request,pk):
    room = Room.objects.get(id=pk)
    serializer = SerializeRoom(room, many=False)
    return Response(serializer.data)