# Generated by Django 3.2.9 on 2021-12-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='optionName',
            field=models.CharField(default='abc', max_length=100),
            preserve_default=False,
        ),
    ]