from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Likes
from .serializers import LikeSerializer
from pelopals.permissions import IsOwnerOrReadOnly


class likes_list(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class likes_detail(generics.RetrieveDestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
