from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/post_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["title", "content", "preview_image", "published"]
    template_name = "blog/post_edit.html"
    success_url = reverse_lazy("post_list")

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.object.id])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("blog:post_list")