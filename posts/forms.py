from django import forms

from posts.models import Post


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your comment here'}))


class CreateUpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
