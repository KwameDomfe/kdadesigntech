# Generated by Django 3.2 on 2023-04-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20221107_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default='_images/placeholders/regular_images/square-01.png', upload_to='images/projects/'),
        ),
    ]