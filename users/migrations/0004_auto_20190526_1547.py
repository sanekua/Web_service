# Generated by Django 2.2.1 on 2019-05-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='files',
            field=models.FileField(default='default.txt', upload_to='pdf'),
        ),
    ]