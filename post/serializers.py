from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

"""
django + reat App은 API 요청을 통해 데이터 주고받음.
이 때 API 요청 및 반환값은 JSON이 대부분.
반환값을 JSON으로 직렬화해주어야 함.
이 때 필요한 것이 DRF의 serializers
"""

# 포스트 시리얼라이저
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'text',
        )
        model = Post

# 회원가입 시리얼라이저
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password'
        )
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user

# 접속 유지중인지 확인하는 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

# 로그인 시리얼라이저
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")