# Generated by Django 3.2.5 on 2021-09-23 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebookapp', '0007_esample_login_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
