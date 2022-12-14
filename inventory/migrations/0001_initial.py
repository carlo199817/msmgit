# Generated by Django 4.1 on 2022-10-04 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_no', models.CharField(blank=True, max_length=200)),
                ('sku', models.CharField(blank=True, max_length=200)),
                ('product', models.CharField(blank=True, max_length=200)),
                ('quantity', models.CharField(blank=True, max_length=200)),
                ('price', models.CharField(blank=True, max_length=200)),
                ('timenow', models.CharField(blank=True, max_length=200)),
                ('datenow', models.CharField(blank=True, max_length=200)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date_updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PosmInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posm_no', models.CharField(blank=True, max_length=200)),
                ('sku', models.CharField(blank=True, max_length=200)),
                ('posm', models.CharField(blank=True, max_length=200)),
                ('quantity', models.CharField(blank=True, max_length=200)),
                ('price', models.CharField(blank=True, max_length=200)),
                ('timenow', models.CharField(blank=True, max_length=200)),
                ('datenow', models.CharField(blank=True, max_length=200)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date_updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
