# Generated by Django 4.0.3 on 2022-04-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0010_alter_adc_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adc',
            name='Version',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
