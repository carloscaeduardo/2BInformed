# -*- coding: utf-8 -*-

from django import forms
from blog.models import Post, Comment
from PIL import Image
from django.core.files import File
class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ("author", "title", "text", "images")
        
        widgets = {
                'title': forms.TextInput(attrs={'class':'textinputclass'}),
                'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            }        
        
class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ("author", "text")
        
        widgets = {
                'author': forms.TextInput(attrs={'class':'textinputclass'}),
                'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea commentcontent'}),
            
            }    