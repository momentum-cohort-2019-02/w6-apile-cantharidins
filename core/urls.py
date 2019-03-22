from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name="post_new"),
]
