from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import MileStone
from .serializers import MileStoneSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def milestone_list(request):
    if request.method == 'GET':
        milestones = MileStone.objects.all()
        serializer = MileStoneSerializer(milestones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MileStoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def milestone_detail(request, id):
    milestone = get_object_or_404(MileStone, pk=id)

    if request.method == 'GET':
        serializer = MileStoneSerializer(milestone)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MileStoneSerializer(milestone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        milestone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
