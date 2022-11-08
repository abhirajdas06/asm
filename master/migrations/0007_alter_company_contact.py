# Generated by Django 4.0.5 on 2022-11-04 11:04

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_alter_vendor_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, region=None),
        ),
    ]
