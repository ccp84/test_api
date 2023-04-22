from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.follower_list.as_view()),
    path('followers/<pk>', views.follower_detail.as_view()),
]
