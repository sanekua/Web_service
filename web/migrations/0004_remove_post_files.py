# Generated by Django 2.1 on 2019-05-28 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_post_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='files',
        ),
    ]
