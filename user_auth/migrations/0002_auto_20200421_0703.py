# Generated by Django 3.0.5 on 2020-04-21 07:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follow',
            new_name='Follower',
        ),
    ]
