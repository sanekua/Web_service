# Generated by Django 2.1 on 2019-05-29 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_remove_post_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='files',
            field=models.FileField(default='default.txt', upload_to=''),
        ),
    ]
