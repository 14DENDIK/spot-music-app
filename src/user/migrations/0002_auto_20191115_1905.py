# Generated by Django 2.2.7 on 2019-11-15 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cite',
            field=models.CharField(default='', max_length=500),
        ),
    ]
