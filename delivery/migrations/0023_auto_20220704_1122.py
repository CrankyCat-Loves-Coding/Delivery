# Generated by Django 3.2 on 2022-07-04 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0022_customer_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(
                choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')],
                max_length=200,
                null=True
            ),
        ),
    ]