from django.urls import path
from .views import (
    Home,
    Discover,
    Search,
)

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('discover', Discover.as_view(), name='discover'),
    path('search', Search.as_view(), name='search'),
]
