# Generated by Django 3.1.7 on 2021-07-21 07:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('POST_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instruction',
            new_name='Post',
        ),
    ]
