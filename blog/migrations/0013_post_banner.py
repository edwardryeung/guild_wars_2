# Generated by Django 4.2.1 on 2023-07-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, help_text='A banner image for the post', null=True, upload_to=''),
        ),
    ]
