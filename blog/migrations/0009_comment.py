"""9th migration"""
# Generated by Django 4.2.1 on 2023-06-20 14:10
"""9th migration""""""
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_topic_post_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=500)),
                ('approved', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments',
                                           to='blog.post')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
