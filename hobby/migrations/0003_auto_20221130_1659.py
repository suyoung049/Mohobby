# Generated by Django 3.2.13 on 2022-11-30 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0002_auto_20221128_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobby',
            name='address_type',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='address',
            field=models.CharField(default='온라인', max_length=100),
        ),
    ]
