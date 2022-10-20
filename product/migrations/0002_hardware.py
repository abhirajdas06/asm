# Generated by Django 4.1.2 on 2022-10-18 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0005_softwaretype'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('barcode', models.CharField(max_length=50)),
                ('serial', models.CharField(max_length=50)),
                ('purchased_on', models.DateField()),
                ('warranty_expiry', models.DateField()),
                ('tpm_expiry', models.DateField()),
                ('status', models.CharField(choices=[('working', 'working'), ('damaged', 'damaged')], max_length=30, null=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.asset_location')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.subcategory')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.vendor')),
            ],
        ),
    ]
