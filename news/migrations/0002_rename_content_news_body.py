# Generated by Django 5.1.6 on 2025-02-27 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='content',
            new_name='body',
        ),
    ]
