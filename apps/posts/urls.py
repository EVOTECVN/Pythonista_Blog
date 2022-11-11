from django.urls import path

from .views import (
    PostDetail,
)

app_name = 'posts'
urlpatterns = [
    path('<str:slug>', PostDetail.as_view(), name='post_detail')
]
