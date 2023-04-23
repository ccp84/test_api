from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from shoutouts.models import Milestone
from followers.models import Followers


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    following_id = serializers.SerializerMethodField()

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Followers.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'name',
            'content',
            'image',
            'following_id',]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']
