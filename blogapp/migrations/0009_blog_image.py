# Generated by Django 2.2.4 on 2019-08-09 09:24

import blogapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_remove_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to=blogapp.models.get_memo_image_path),
        ),
    ]