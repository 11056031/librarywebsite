# Generated by Django 4.2.6 on 2024-01-10 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_remove_post_photo_link_post_photolink_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_borrowed',
        ),
        migrations.AddField(
            model_name='post',
            name='isBorrow',
            field=models.BooleanField(default=False, verbose_name='外借中'),
        ),
    ]
