from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from shoutouts.models import Milestone


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'name',
            'content',
            'image',]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']
