# Generated by Django 3.1.2 on 2020-11-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_snippet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.TextField(blank=True, null=True),
        ),
    ]