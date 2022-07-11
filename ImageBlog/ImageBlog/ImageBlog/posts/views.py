from django.views.generic import ListView, CreateView, DetailView, \
    UpdateView
from .models import Post
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, RequestContext
from django.urls import reverse_lazy
from .forms import PostForm, ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from rest_framework import viewsets
from . import serializers


class HomePageView(LoginRequiredMixin, ListView):
    paginate_by = 5
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


class SearchResultsView(LoginRequiredMixin, ListView):
    paginate_by = 5
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query))
        return object_list


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['protowiecgithub@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('email_sent')
    return render(request, 'email.html', {'form': form})

def successView(request):
    return render(request, 'email_sent.html')


class PostViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
