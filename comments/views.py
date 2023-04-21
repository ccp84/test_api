from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Comments
from .serializers import CommentSerializer, CommentDetailSerializer
from pelopals.permissions import IsOwnerOrReadOnly


class comments_list(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class comments_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
