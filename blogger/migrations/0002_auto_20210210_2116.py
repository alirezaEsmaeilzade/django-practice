# Generated by Django 3.1.6 on 2021-02-10 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='created',
        ),
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated',
        ),
    ]
