# Generated by Django 2.2.7 on 2021-01-15 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20201122_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet_image',
            field=models.ImageField(blank=True, help_text={'use images in 3x2 proportion!'}, null=True, upload_to=''),
        ),
    ]