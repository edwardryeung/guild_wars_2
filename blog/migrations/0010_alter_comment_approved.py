"""10th migration """
# Generated by Django 4.2.1 on 2023-06-20 14:29

from django.db import migrations, models

class Migration(migrations.Migration):
"""10 minute migration"""
    dependencies = [
        ('blog', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
