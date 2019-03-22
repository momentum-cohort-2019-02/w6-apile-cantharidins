from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, User, Comment, Vote
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from .forms import CommentForm

def index(request):
    """View function for home page of site."""

    post_list = Post.objects.all()
    vote_counter = Vote.objects.all()
    user = User.objects.all()

    context = {
        'post_list': post_list,
        'vote_counter': vote_counter,
        'user': user,
    }
    # Render the HTML template index.html with the date in the context variable
    return render(request, 'index.html', context=context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment_list = Comment.objects.all()
    context = {
        'post': post,
        'comment_list': comment_list,
    }

    return render(request, 'core/post_details.html', context=context)


def comment_new(request, slug):
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:

        form = CommentForm()
    return render(request, 'core/comment_add.html', {'form': form})