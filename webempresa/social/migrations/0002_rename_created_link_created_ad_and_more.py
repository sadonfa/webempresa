# Generated by Django 4.1.1 on 2022-09-30 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='created',
            new_name='created_ad',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='updated',
            new_name='updated_ad',
        ),
    ]
