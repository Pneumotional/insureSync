# Generated by Django 5.0.3 on 2024-11-20 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_userprofile_full_name_userprofile_first_namme_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_namme',
            new_name='first_name',
        ),
    ]