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
