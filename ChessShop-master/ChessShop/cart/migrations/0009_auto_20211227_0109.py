# Generated by Django 3.2.9 on 2021-12-26 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20211227_0043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverymethod',
            old_name='arrivesWithinMax',
            new_name='arrivesWithinMaxDays',
        ),
        migrations.RenameField(
            model_name='deliverymethod',
            old_name='arrivesWithinMin',
            new_name='arrivesWithinMinDays',
        ),
    ]
