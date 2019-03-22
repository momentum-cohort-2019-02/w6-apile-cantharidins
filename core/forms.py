from django import forms
from .models import Post, Comment, Profile, Vote

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ("content",)

