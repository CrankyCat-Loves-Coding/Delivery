# Generated by Django 3.2 on 2022-07-04 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0032_remove_ordermodel_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='transaction_id',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
