# Generated by Django 2.2.5 on 2019-09-24 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamfile',
            name='file',
            field=models.FileField(upload_to='teamfiles/'),
        ),
    ]
