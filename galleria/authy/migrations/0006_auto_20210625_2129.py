# Generated by Django 3.1 on 2021-06-25 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0005_auto_20210625_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='url',
            new_name='email',
        ),
    ]