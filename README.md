# Project development

* Install django `pip install 'django<4'`
* Install rest `pip install djangorestframework` add rest_framework to installed apps list
* Start your project `django-admin startproject pelopals .`
* Create app `python manage.py startapp pelofondo`
* Add app to settings.py
* Create Procfile include `web: gunicorn pelopals.wsgi`
* Migrate (throughout) `python manage.py migrate`
* Create superuser `python manage.py createsuperuser`
* Add models - makemigrations - migrate - add to admin
* Add serializers.py
```python
from rest_framework import serializers
from .models import Ride


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'name', 'description', 'stacktime', 'stackleader']
```
* Create the view to serialize the data
```python
from django.shortcuts import render
from django.http import JsonResponse
from .models import Ride
from .serializers import RideSerializer


# Create your views here.
def ride_list(request):
    rides = Ride.objects.all()
    serializer = RideSerializer(rides, many=True)
    return JsonResponse({'data': serializer.data}) //returns an object
```
* Create URL for app
```python
from django.urls import path
from pelofondo import views

urlpatterns = [
    path('rides/', views.ride_list),
]
```
* Import app URLs into project URLS
```python
from django.contrib import admin
from django.urls import path, include
from pelofondo import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pelofondo.urls'), name='pelofondo_urls')
]
```
* URL returns data : https://rest-tutorial.herokuapp.com/rides/

## CRUD Capability

* Import api_decorators to use with views
```python
from rest_framework.decorators import api_view <<New import


# Create your views here.
@api_view(['GET', 'POST']) <<New decorator
def ride_list(request):
```

* Add Post functionality to view - Use if statements to check method being used 
```python
from rest_framework.response import Response << New import
from rest_framework import status << New import

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
```