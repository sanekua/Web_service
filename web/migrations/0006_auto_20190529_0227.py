# Generated by Django 2.1 on 2019-05-29 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_post_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='files',
            field=models.FileField(upload_to='books/pdfs/'),
        ),
    ]
