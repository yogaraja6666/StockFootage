# Generated by Django 4.2.4 on 2023-08-09 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_post_delete_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(default='nature', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='nature', max_length=100),
        ),
    ]
