from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/comment', views.comment_new, name='comment_new'),
]
