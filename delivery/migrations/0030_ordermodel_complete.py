# Generated by Django 3.2 on 2022-07-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0029_alter_ordermodel_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
