# Generated by Django 3.2 on 2022-09-12 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20220904_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectoverview',
            name='title',
        ),
        migrations.AddField(
            model_name='projectoverview',
            name='description',
            field=models.TextField(default='Project Overview', max_length=256),
        ),
    ]