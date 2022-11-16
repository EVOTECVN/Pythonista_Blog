from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Post


class PostDetail(View):
    template_name = 'posts/detail.html'

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(slug=slug)
        post = get_object_or_404(queryset)
        return render(request, self.template_name, context={
            'post': post
        })
