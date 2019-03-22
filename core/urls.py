from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('This should contain a link to the specific post?', views.comment_detail, name='comment_detail'),
]
