# Generated by Django 4.0.5 on 2022-11-22 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
        ('product', '0007_hardware_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardware',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='master.branch'),
        ),
    ]
