# Generated by Django 3.2.13 on 2022-07-06 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valdata', '0005_auto_20220703_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='cvat_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
