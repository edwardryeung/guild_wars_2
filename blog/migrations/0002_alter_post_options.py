# Generated by Django 4.2.1 on 2023-06-14 08:24
"""second migration"""
from django.db import migrations


class Migration(migrations.Migration):
"""second migration"""
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
    ]
