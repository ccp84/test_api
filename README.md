# Project development

[Course here](https://www.youtube.com/watch?v=i5JykvxUk_A)

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
* For a read only field add this before Meta `owner = serializers.ReadOnlyField(source='owner.username')`

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
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

* Add ride detail view
* Create detail URL - `path('rides/<int:id', views.ride_detail),`
* Create the view:
```python
from django.shortcuts import get_object_or_404 << new import

@api_view(['GET', 'PUT', 'DELETE'])
def ride_detail(request, id):
    ride = get_object_or_404(Ride, pk=id)

    if request.method == 'GET':
        serializer = RideSerializer(ride)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RideSerializer(ride, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ride.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

## Media and Static on AWS
* [Course here](https://www.youtube.com/watch?v=f64Ue2C39Ag)
* Install pillow, django-storages, boto3 `pip install Pillow django-storages boto3`
* Add storeages to installed apps
* Create media folder in root
* In settings - import os and set media :
```python
# Add settings for env
if os.path.isfile("env.py"):
   import env

# AWS S3

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')

AWS_STORAGE_BUCKET_NAME = 'pelopals'

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

AWS_DEFAULT_ACL = 'public-read'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}

AWS_LOCATION = 'static'

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {
    'Access-Control-Allow-Origin': '*',
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
```
* In models - add image field `image = models.ImageField(upload_to='media/')`

* Create env : `os.environ["KEY"] =`

## Creating model signals

* Add imports to top of models `from django.db.models.signals import post_save`
* Write function:
```python
# Signal connecting to User on save
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile(sender=User))
```

## Converting to class views with mixins
* [Resource here](https://www.django-rest-framework.org/tutorial/3-class-based-views/)
* Import `from rest_framework import generics`
* Build CBV:
```python
class profile_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
```

## Add REST auth login URL path
* `path('api-auth/', include('rest_framework.urls')),`

## Using generic permissions mixin:
* Import to views `from rest_framework import permissions`
* Add line to any CBV that you want to use it `permission_classes = [permissions.IsAuthenticatedOrReadOnly]`

## Creating custom permissions:
```python
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
```
* Import `from pelopals.permissions import IsOwnerOrReadOnly`
* Use `permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly] / IsAuthenticated`

## To auto link an owner of a post - [source](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/)

* In views within the class add:
```python
def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```
* To the model add:
```python
owner = models.ForeignKey(
        User, related_name='milestones', on_delete=models.CASCADE)
```