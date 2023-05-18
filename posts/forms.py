from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your comment here'}))
