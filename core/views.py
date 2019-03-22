from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, User, Comment, Vote
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from core.forms import PostForm
import datetime
from django.forms.widgets import TextInput


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
    
    context = {
        'post': post,
    }

    return render(request, 'core/post_details.html', context=context)


# @login_required
def post_new(request):
    
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.date_posted = datetime.datetime.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'core/post_edit.html', {'form': form})

@login_required    
def post_vote_view(request, slug):   
    post = get_object_or_404(Post, slug=slug)

    vote, created = request.user.vote_set.get_or_create(post=post)

    if created:
        messages.success(request, f"You have voted for {post.title}.")
    else:
        messages.info(request, f"You have unvoted for {post.title}.")
        vote.delete()

    return redirect('post_detail', slug)   
    
    
