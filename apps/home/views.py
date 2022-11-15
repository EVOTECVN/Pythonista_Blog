from django.views import View
from django.shortcuts import render
from django.contrib.postgres.search import SearchVector

from apps.posts.models import (
    Post
)


class Home(View):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, self.template_name, context={
            'posts': posts
        })


class Discover(View):
    template_name = 'home/discover.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class Search(View):
    template_name = 'home/search.html'

    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword')
        posts = Post.objects.annotate(
            search=SearchVector('title', 'tags__name', 'tags__title', 'description', 'content')).filter(
            search=keyword)
        return render(request, self.template_name, context={
            'keyword': keyword,
            'posts': posts,
        })
