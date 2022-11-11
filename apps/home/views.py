from django.views import View
from django.shortcuts import render

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
