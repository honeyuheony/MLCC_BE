# Generated by Django 3.2.13 on 2022-07-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valdata', '0006_data_cvat_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('dt', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]