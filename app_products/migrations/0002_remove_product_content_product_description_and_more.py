# Generated by Django 4.0.2 on 2022-02-28 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='content',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
