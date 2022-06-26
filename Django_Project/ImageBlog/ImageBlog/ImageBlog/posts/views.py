from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(ListView):
    paginate_by = 2
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.order_by('-created_date')


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')


class ShowPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('post_detail')


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text', 'picture']
    template_name = 'post_edit.html'
    success_url = reverse_lazy('home')
