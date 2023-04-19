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
    return JsonResponse(serializer.data, safe=False)
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