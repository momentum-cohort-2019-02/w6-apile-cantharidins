from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/comment', views.comment_new, name='comment_new'),
    path('post/new/', views.post_new, name="post_new"),
    path('post/<slug:slug>/vote', views.post_vote_view, name="post_vote"),
    path('post/<slug:slug>/remove', views.post_remove, name='post_remove'),
    path('post/<slug:slug>/comment/remove', views.comment_remove, name='comment_remove'),
]
