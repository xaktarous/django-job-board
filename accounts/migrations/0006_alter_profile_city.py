# Generated by Django 5.1.5 on 2025-01-30 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_city_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_city', to='accounts.city'),
        ),
    ]
