from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import View,DetailView,ListView,DeleteView,UpdateView,CreateView,TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'hello/index.html'

class PostListView(ListView):
    context_object_name = 'posts'
    model = models.Post
    template_name = 'hello/post_list.html'

class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = models.Post
    template_name = 'hello/post_detail.html'

class PostCreateView(CreateView):
    fields = ("Title","Text_description")
    model = models.Post

class PostUpdateView(UpdateView):
    fields = ("Title","Text_description")
    model = models.Post

class PostDeleteView(DeleteView):
    model = models.Post
    success_url = reverse_lazy('hello:list')
