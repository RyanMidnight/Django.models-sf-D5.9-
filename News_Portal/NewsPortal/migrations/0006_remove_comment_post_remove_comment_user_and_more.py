# Generated by Django 4.1.5 on 2023-01-16 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='postcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='postcategory',
            name='post',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostCategory',
        ),
    ]
