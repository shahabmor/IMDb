# Generated by Django 4.1.2 on 2022-11-18 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.DeleteModel(
            name='Relation',
        ),
    ]
