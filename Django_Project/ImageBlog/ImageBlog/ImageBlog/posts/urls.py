from django.urls import path
from .views import HomePageView, CreatePostView, ShowPostView, EditPostView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='post'),
    path('post/<int:pk>/', ShowPostView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', EditPostView.as_view(), name='post_edit'),
]
