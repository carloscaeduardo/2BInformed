from django.db import models

from django.utils import timezone
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields  import RichTextUploadingField
from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT
from hitcount.models import HitCount


# Create your models here.



class Post(models.Model, HitCountMixin):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = RichTextUploadingField(config_name='default',
                external_plugin_resources=[(
                                                'youtube',
                   '/static/ckeditor/ckeditor/plugins/youtube/',
                                                'plugin.js',

                                                            )]
                                                                )


    snippet_image = models.ImageField(blank = True, null = True, help_text={"use images in 3x2 proportion!" })
    created_date = models.DateTimeField(default = timezone.now)
    publication_date = models.DateTimeField(blank = True, null=True)
    slug = models.SlugField(allow_unicode=True, unique = True)
    subject = models.CharField(max_length= 200, blank = True, null = True)
    hit_count_generic = GenericRelation(
        MODEL_HITCOUNT, object_id_field='slug',
        related_query_name='hit_count_generic_relation')

    def publish(self):
        self.publication_date = timezone.now()

        self.save()

    def hitcount(self):
        hit_count = HitCount.objects.get_for_object(self)
        return hit_count

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs = {'slug':self.slug })



