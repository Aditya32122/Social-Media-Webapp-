# Generated by Django 5.1.4 on 2024-12-29 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_remove_tweet_likes_count_tweet_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='likes',
        ),
    ]
