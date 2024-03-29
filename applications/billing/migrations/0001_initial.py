# Generated by Django 5.0.1 on 2024-01-10 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('unit_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('debt', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('total', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.client')),
                ('paleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.paletainventory')),
            ],
        ),
    ]
