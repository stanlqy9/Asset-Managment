# Generated by Django 5.0.6 on 2024-07-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='puchase_date',
            new_name='purchase_date',
        ),
        migrations.AlterField(
            model_name='asset',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='asset',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]