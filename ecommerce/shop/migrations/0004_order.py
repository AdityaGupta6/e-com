# Generated by Django 3.2.4 on 2021-07-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(default='', max_length=10000)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('locality', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=1000)),
                ('state', models.CharField(default='', max_length=1000)),
                ('zip', models.CharField(default='', max_length=1000)),
                ('phone', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
