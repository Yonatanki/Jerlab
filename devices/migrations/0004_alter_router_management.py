# Generated by Django 4.0.3 on 2022-04-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_alter_adc_router_management'),
    ]

    operations = [
        migrations.AlterField(
            model_name='router',
            name='Management',
            field=models.GenericIPAddressField(unique=True),
        ),
    ]
