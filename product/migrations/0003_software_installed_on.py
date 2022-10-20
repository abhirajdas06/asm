# Generated by Django 4.1.2 on 2022-10-18 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_hardware'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='installed_on',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.hardware'),
        ),
    ]
