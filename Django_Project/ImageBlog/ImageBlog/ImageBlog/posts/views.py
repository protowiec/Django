from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')


class ShowPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('post_detail')


class EditPostView(UpdateView):
    model = Post
    fields = ['title', 'text', 'picture']
    template_name = 'post_edit.html'
    success_url = reverse_lazy('home')
