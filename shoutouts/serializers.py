from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Milestone


class MilestoneSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Milestone
        fields = ['id', 'title', 'image', 'owner']
