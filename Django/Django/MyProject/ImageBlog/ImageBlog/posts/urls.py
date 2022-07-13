from django.contrib import admin
from django.urls import path, include
from .views import (
    HomePageView,
    CreatePostView,
    ShowPostView,
    EditPostView,
    SearchResultsView,
    contactView,
    successView,
    postLike,
)
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostViewset)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='post'),
    path('post/<int:pk>/', ShowPostView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', EditPostView.as_view(), name='post_edit'),
    path('post_like/<int:pk>', postLike, name='post_like'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('email/', contactView, name='email'),
    path('email_sent/', successView, name='email_sent'),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
]
