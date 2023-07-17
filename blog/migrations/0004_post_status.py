# Generated by Django 4.2.1 on 2023-06-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft',
                                   help_text='Set to "published" to make this post publicly visible', max_length=10),
        ),
    ]
