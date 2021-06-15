# Generated by Django 3.1.6 on 2021-06-15 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0036_auto_20210615_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='content_length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='http_status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='is_cdn',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='is_imported_subdomain',
            field=models.BooleanField(default=False),
        ),
    ]
