from django.urls import path
from shoutouts import views

urlpatterns = [
    path('milestones/', views.milestone_list),
    path('milestones/<id>', views.milestone_detail),
]
