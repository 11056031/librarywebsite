# Generated by Django 4.2.6 on 2023-11-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_post_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='team',
            field=models.CharField(default='YourDefaultValueHere', max_length=200),
        ),
    ]
