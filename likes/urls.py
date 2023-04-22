from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.likes_list.as_view()),
    path('likes/<pk>', views.likes_detail.as_view()),
]
