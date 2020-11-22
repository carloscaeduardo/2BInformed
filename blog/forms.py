# -*- coding: utf-8 -*-

from django import forms
from blog.models import Post
from PIL import Image
from django.core.files import File
from mediumeditor.widgets import MediumEditorTextarea
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    text = forms.CharField(widget=forms.Textarea)
    
    class Meta():
        model = Post
        fields = ("author", "title", "text", "snippet_image", "subject")
        
        widgets = {
                'title': forms.TextInput(attrs={'class':'textinputclass'}),
                'text': RichTextUploadingField(),
            }        

    
    