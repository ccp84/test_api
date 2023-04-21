from rest_framework import serializers
from .models import Comments


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    class Meta:
        model = Comments
        fields = [
            'owner',
            'milestone',
            'created_at',
            'updated_at',
            'content',
            'profile_id',
            'profile_image'
        ]


class CommentDetailSerializer(CommentSerializer):
    milestone = serializers.ReadOnlyField(source='milestone.id')
