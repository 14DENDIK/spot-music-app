# Generated by Django 2.2.7 on 2019-11-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_song_is_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(default='pop', max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='music',
            field=models.FileField(null=True, upload_to='music'),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(default='music', max_length=200),
        ),
    ]
