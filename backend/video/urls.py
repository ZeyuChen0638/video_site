from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("recommand/", recommand, name="recommand"),
    path("avatar/", AvatarAPIView.as_view(), )
]