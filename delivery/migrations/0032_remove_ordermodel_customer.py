# Generated by Django 3.2 on 2022-07-04 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0031_ordermodel_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='customer',
        ),
    ]