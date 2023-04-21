from django.shortcuts import render, get_object_or_404
from .models import Milestone
from .serializers import MilestoneSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from pelopals.permissions import IsOwnerOrReadOnly


# Create your views here.
# @api_view(['GET', 'POST'])
# def milestone_list(request):
#     if request.method == 'GET':
#         milestones = Milestone.objects.all()
#         serializer = MilestoneSerializer(milestones, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MilestoneSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class milestone_list(generics.ListCreateAPIView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET', 'PUT', 'DELETE'])
def milestone_detail(request, id):
    milestone = get_object_or_404(Milestone, pk=id)

    if request.method == 'GET':
        serializer = MilestoneSerializer(milestone)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MilestoneSerializer(milestone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        milestone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
