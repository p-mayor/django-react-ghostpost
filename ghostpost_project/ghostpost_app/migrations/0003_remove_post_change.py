# Generated by Django 3.0 on 2019-12-30 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0002_auto_20191230_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='change',
        ),
    ]
