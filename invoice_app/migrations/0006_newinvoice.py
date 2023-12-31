# Generated by Django 4.2.2 on 2023-07-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0005_product_cgst_product_igst_product_sgst'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('purchase_order_number', models.CharField(max_length=100)),
                ('vendor_code', models.CharField(max_length=100)),
                ('invoice_date', models.CharField(max_length=100)),
                ('purchase_id', models.CharField(max_length=100)),
                ('purchase_date', models.CharField(max_length=100)),
                ('no_of_units_allowed', models.CharField(max_length=100)),
                ('cost_per_unit', models.CharField(max_length=100)),
                ('invoice_no', models.CharField(max_length=100)),
            ],
        ),
    ]
