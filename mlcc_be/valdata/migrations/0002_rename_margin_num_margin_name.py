# Generated by Django 3.2.13 on 2022-06-26 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='margin',
            old_name='margin_num',
            new_name='name',
        ),
    ]