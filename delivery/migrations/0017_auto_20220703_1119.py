# Generated by Django 3.2 on 2022-07-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0016_alter_ordermodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='eircode',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
