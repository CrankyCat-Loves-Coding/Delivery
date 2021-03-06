# Generated by Django 3.2 on 2022-06-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0010_auto_20220627_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_paid', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(blank=True, related_name='order', to='delivery.Menu')),
            ],
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
