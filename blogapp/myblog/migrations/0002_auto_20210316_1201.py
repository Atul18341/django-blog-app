# Generated by Django 3.1.7 on 2021-03-16 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='post',
            new_name='content',
        ),
    ]
