# Generated by Django 5.1.4 on 2025-01-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0007_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
