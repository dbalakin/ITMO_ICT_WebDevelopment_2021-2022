# Generated by Django 4.0.1 on 2022-01-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bonus_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.URLField(blank=True),
        ),
    ]
