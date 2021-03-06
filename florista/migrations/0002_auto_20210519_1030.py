# Generated by Django 3.2.3 on 2021-05-19 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('florista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False, null=True)),
                ('date_added', models.DateTimeField(auto_now=True, null=True)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=15, null=True)),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='florista.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=15, null=True)),
                ('is_ordered', models.BooleanField(default=False, null=True)),
                ('date_ordered', models.DateTimeField(auto_now=True, null=True)),
                ('items', models.ManyToManyField(to='florista.CartItem')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
