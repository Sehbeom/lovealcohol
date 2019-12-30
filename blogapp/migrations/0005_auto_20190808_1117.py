# Generated by Django 2.2.4 on 2019-08-08 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20190808_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_data',
            field=models.DateTimeField(verbose_name='data published'),
        ),
    ]
