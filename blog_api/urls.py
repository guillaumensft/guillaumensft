from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import (

    ArticleViewSet,
)

from blog.views import ArticleListView, ArticleDetailView
app_name = 'blog_api'

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
