from django.urls import path
from pelofondo import views

urlpatterns = [
    path('rides/', views.ride_list),
    path('rides/<id>', views.ride_detail),
]
