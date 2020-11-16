from django.db import models

from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    images = models.ImageField(upload_to='media/', null = True, blank=True)
    created_date = models.DateTimeField(default = timezone.now)
    publication_date = models.DateTimeField(blank = True, null=True)
    slug = models.SlugField(allow_unicode=True, unique = True)
    not_published = True
    def publish(self):
        self.publication_date = timezone.now()
        self.not_published = False
        self.save()
        
    def approve_comments(self):
        return self.comments.filter(approved_comment = True)
 
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("post_detail", kwargs = {'slug':self.slug })
    
    
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name = 'comments', on_delete=models.CASCADE)
    author = models.CharField(max_length = 200)
    text= models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default = False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
        
    def get_absolute_url(self):
        return('post_list')
        
    def __str__(self):
        return self.text
        
    