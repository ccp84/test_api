from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.profile_list.as_view()),
    path('profiles/<pk>', views.profile_detail.as_view()),
    path('users/', views.user_list.as_view()),
    path('users/<pk>', views.user_detail.as_view()),
]
