from django.urls import path

from .views import (
    PostListAPI,
)


app_name = 'api'

urlpatterns = [
    path('posts', PostListAPI.as_view(), name='posts')
]
