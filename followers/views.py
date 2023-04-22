from rest_framework import generics, permissions
from .models import Followers
from .serializers import FollowerSerializer
from pelopals.permissions import IsOwnerOrReadOnly


class follower_list(generics.ListCreateAPIView):
    queryset = Followers.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class follower_detail(generics.RetrieveDestroyAPIView):
    queryset = Followers.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
