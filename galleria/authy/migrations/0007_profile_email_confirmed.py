# Generated by Django 3.1 on 2021-06-28 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0006_auto_20210625_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
