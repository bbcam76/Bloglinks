""" URL Configuration for blog app. """
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.PostList.as_view(), name="blog"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
