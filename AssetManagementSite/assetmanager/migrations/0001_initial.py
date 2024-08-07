# Generated by Django 5.0.6 on 2024-07-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_tag', models.IntegerField()),
                ('display_name', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=15)),
                ('puchase_date', models.DateField()),
                ('purchase_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('assigned_to', models.CharField(max_length=50)),
                ('warranty_expiration', models.DateField()),
                ('notes', models.TextField()),
            ],
        ),
    ]
