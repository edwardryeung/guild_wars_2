# Generated by Django 4.2.1 on 2023-07-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_contestsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoContestSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(upload_to='')),
                ('submitted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-submitted'],
            },
        ),
        migrations.DeleteModel(
            name='ContestSubmission',
        ),
    ]
