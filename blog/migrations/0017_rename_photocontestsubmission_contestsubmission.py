# Generated by Django 4.2.1 on 2023-07-23 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_photocontestsubmission_delete_contestsubmission'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PhotoContestSubmission',
            new_name='ContestSubmission',
        ),
    ]