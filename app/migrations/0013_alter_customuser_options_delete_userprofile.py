# Generated by Django 5.0 on 2024-03-09 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]