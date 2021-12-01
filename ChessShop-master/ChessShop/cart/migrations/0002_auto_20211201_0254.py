# Generated by Django 3.2.9 on 2021-11-30 23:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverydata',
            name='arrivesWithinMax',
        ),
        migrations.RemoveField(
            model_name='deliverydata',
            name='arrivesWithinMin',
        ),
        migrations.RemoveField(
            model_name='deliverydata',
            name='deliveryCost',
        ),
        migrations.AddField(
            model_name='deliverymethod',
            name='arrivesWithinMax',
            field=models.DurationField(default=datetime.timedelta(days=1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deliverymethod',
            name='arrivesWithinMin',
            field=models.DurationField(default=datetime.timedelta(days=1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deliverymethod',
            name='costNote',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deliverymethod',
            name='deliveryCost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]