# Generated by Django 4.0.4 on 2022-05-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0014_alter_adc_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adc',
            name='Console',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='adc',
            name='Management_Port',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='adc',
            name='Management_Vlan',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]