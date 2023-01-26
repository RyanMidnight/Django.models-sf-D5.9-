# Generated by Django 4.1.5 on 2023-01-22 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NewsPortal', '0022_remove_comment_post_remove_comment_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.FloatField(default=0.0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_or_news', models.CharField(choices=[('Post', 'Post'), ('News', 'News')], default='Post', max_length=4)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('headline', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('rating', models.FloatField(default=0.0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(through='NewsPortal.PostCategory', to='NewsPortal.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.FloatField(default=0.0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]