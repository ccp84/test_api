from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from pelopals.permissions import IsOwnerOrReadOnly


# Create your views here.
class profile_list(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


# class profile_detail(APIView):
#     serializer_class = ProfileSerializer
#     def get(self, request, pk):
#         profile = get_object_or_404(Profile, pk=pk)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         profile = get_object_or_404(Profile, pk=pk)
#         serializer = ProfileSerializer(profile)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serislizer.data, status=status.HTTP_200_OK)
#         return Response(
#               serializer._errors, status=status.HTTP_400_BAD_REQUEST)

class profile_detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class user_list(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class user_detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
