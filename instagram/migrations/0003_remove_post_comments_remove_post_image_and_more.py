# Generated by Django 5.1.7 on 2025-03-25 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
    ]
