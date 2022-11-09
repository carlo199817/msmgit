# Generated by Django 4.1 on 2022-10-04 08:38

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
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(blank=True, max_length=200)),
                ('timenow', models.CharField(blank=True, max_length=200)),
                ('datenow', models.CharField(blank=True, max_length=200)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date_updated')),
                ('latitude', models.CharField(blank=True, max_length=200)),
                ('longitude', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/%Y/%m/%d/')),
                ('gender', models.CharField(blank=True, max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('quantity', models.CharField(blank=True, max_length=200)),
                ('price', models.CharField(blank=True, max_length=200)),
                ('sproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sproduct', to='store.store')),
            ],
        ),
        migrations.CreateModel(
            name='SPosm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('quantity', models.CharField(blank=True, max_length=200)),
                ('price', models.CharField(blank=True, max_length=200)),
                ('sposm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sposm', to='store.store')),
            ],
        ),
    ]
