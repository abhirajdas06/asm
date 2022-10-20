# Generated by Django 4.1.2 on 2022-10-13 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_active_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_location',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='users.branch'),
            preserve_default=False,
        ),
    ]
