# Generated by Django 2.2.7 on 2019-11-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_remove_song_is_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
    ]
