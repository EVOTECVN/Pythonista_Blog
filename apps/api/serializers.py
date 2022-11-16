from rest_framework import serializers

from apps.posts.models import (
    Post,
)


class PostSerializers(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()
