from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.comments_list.as_view()),
    path('comments/<pk>', views.comments_detail.as_view()),
]
