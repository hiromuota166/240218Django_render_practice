# myapp/serializers.py
from rest_framework import serializers
from .models import Post

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # ここでシリアライズするフィールドを指定します
