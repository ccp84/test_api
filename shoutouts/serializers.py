from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Milestone
from likes.models import Likes


class MilestoneSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    like_id = serializers.SerializerMethodField()

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            milestone = Likes.objects.filter(
                owner=user, milestone=obj
            ).first()
            return milestone.id if milestone else None
        return None

    class Meta:
        model = Milestone
        fields = ['id', 'title', 'image', 'owner', 'like_id']
