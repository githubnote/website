# Generated by Django 2.2.5 on 2019-10-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageWorker', '0002_auto_20191023_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_info',
            name='site_name',
            field=models.CharField(max_length=100),
        ),
    ]