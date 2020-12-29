from .models import Comment
from django import forms

# adding comments including name and mail of the user % the comment itself


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
