from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from .models import Post
from .serializers import (
    PostSerializer,
)

# Create your views here.

class PostVeiwSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(setlf):
        return Post.objects.all()
