from django.shortcuts import render
from django.http import JsonResponse
from .models import Ride
from .serializers import RideSerializer


# Create your views here.
def ride_list(request):
    rides = Ride.objects.all()
    serializer = RideSerializer(rides, many=True)
    return JsonResponse(serializer.data)
