from django.contrib import admin
from blog.models import Post
from blog import models
from mediumeditor.admin import MediumEditorAdmin

# Register your models here.



class PostAdmin(MediumEditorAdmin, admin.ModelAdmin):
    """

    """
    fields=['title', 'author','subject', 'created_date','publication_date','snippet_image',  'text' ]
    search_fields = ['title', 'subject']
    mediumeditor_fields = ('my_text_field', )
    list_display = ['title', 'author','subject', 'created_date','publication_date' ]



admin.site.register(models.Post, PostAdmin)