from django.contrib.auth.models import User
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from rest_framework import status, generics, permissions, filters
from rest_framework.response import Response
from pelopals.permissions import IsOwnerOrReadOnly


class profile_list(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        milestones_count=Count('owner__milestones', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__followed', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'milestones_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]
    serializer_class = ProfileSerializer


class profile_detail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class user_list(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class user_detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
