from django.db import models

from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields  import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = RichTextUploadingField()
    snippet_image = models.ImageField(blank = True, null = True)
    created_date = models.DateTimeField(default = timezone.now)
    publication_date = models.DateTimeField(blank = True, null=True)
    slug = models.SlugField(allow_unicode=True, unique = True)
    subject = models.CharField(max_length= 200, blank = True, null = True)
    def publish(self):
        self.publication_date = timezone.now()
        
        self.save()
     
       
 
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("post_detail", kwargs = {'slug':self.slug })
    
     

