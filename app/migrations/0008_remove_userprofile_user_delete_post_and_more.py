# Generated by Django 5.0 on 2024-03-08 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_userprofile_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]