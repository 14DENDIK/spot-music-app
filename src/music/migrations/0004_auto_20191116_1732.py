# Generated by Django 2.2.7 on 2019-11-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_album_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='extension',
        ),
        migrations.AddField(
            model_name='song',
            name='music',
            field=models.FileField(default='music.mp3', upload_to='music'),
        ),
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.FileField(default='album_default.jpg', upload_to='album_images'),
        ),
    ]