# Generated by Django 3.0 on 2019-12-30 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0003_remove_post_change'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='votes',
            new_name='likes',
        ),
    ]