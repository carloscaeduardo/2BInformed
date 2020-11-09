from django.contrib import admin
from blog.models import Post, Comment
from blog import models

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    """  
    
    """
    fields=['title', 'author', 'created_date','publication_date', 'images', 'text']
    search_fields = ['title']
    
    
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)