# Generated by Django 3.2 on 2022-07-03 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0015_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
