# Generated by Django 2.1.15 on 2024-04-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20240419_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='alternate_mobile_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='primary_mobile_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
