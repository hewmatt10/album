# Generated by Django 4.0 on 2022-05-22 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album_site', '0004_album_user_alter_album_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='size',
        ),
    ]
