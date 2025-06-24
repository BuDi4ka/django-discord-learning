from rest_framework import serializers

from base.models import Room



class RoomSerializer(serializers.ModelSerializer):
    host = serializers.CharField(source='host.username', read_only=True)
    topic = serializers.CharField(source='topic.name', read_only=True)
    participants = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Room
        fields = '__all__'
