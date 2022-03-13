from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import ArticleSerializer
from blog.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('titre')
    serializer_class = ArticleSerializer
