from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class EmailSerializer(serializers.Serializer):
    from_email = serializers.EmailField()
    to_email = serializers.EmailField()
    name = serializers.CharField()
    comments = serializers.CharField()