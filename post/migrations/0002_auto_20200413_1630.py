# Generated by Django 3.0.5 on 2020-04-13 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
