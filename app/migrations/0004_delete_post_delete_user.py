# Generated by Django 5.0 on 2024-03-07 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_user_email_remove_user_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
