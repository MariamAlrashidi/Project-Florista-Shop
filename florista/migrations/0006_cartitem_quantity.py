# Generated by Django 3.2.3 on 2021-05-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('florista', '0005_alter_cartitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
