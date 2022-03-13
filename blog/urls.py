from django.contrib import admin
from django.urls import path, include

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    DeleteArticle,
    UserProfileDetailView,
)
app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='post-list'),
    path('create/', ArticleCreateView.as_view(), name='post-create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='post-detail'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='post-update'),
    path('<int:id>/delete/', ArticleUpdateView, name='post-delete'),

]



urlpatterns += [

    path('users/<int:id>/', UserProfileDetailView.as_view(), name='userprofile-detail'),

]
