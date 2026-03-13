from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views import View
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog/post_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(published=True)


class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "content", "preview_image", "published", "views_count"]
    template_name = "blog/post_create.html"
    success_url = reverse_lazy("blog:post_list")
