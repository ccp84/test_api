from rest_framework import serializers
from .models import MileStone


class MileStoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = MileStone
        fields = ['id', 'title', 'image']
