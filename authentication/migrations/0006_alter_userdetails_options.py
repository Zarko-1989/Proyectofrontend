# Generated by Django 4.0.6 on 2022-10-13 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_userdetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userdetails',
            options={'verbose_name_plural': 'UserDetails'},
        ),
    ]
