# Generated by Django 4.0.5 on 2022-11-21 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_hardware_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
