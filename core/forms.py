from django import forms
from core.models import Post, Comment, Vote

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'post_url', 'description')



# class NewCommentForm(forms.Form):
#     comment = forms.CharField(        
#     )

#     class Meta:
#         model = Comment