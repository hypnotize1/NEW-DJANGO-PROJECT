from django import forms
from Blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'subject', 'message', 'email']