from django.shortcuts import render
from django.http import JsonResponse
from .models import Ride
from .serializers import RideSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def ride_list(request):
    if request.method == 'GET':
        rides = Ride.objects.all()
        serializer = RideSerializer(rides, many=True)
        return JsonResponse({'data': serializer.data})

    if request.method == 'POST':
        serializer = RideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
