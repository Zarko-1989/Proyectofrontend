# Generated by Django 4.0.6 on 2022-09-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Earth', max_length=100),
        ),
    ]
