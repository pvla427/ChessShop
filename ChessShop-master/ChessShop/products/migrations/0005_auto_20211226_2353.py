# Generated by Django 3.2.9 on 2021-12-26 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20211226_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chessboard',
            name='driveType',
            field=models.CharField(default='шаговый', max_length=100),
        ),
        migrations.AlterField(
            model_name='chessboard',
            name='powerW',
            field=models.FloatField(default=30.0),
        ),
        migrations.AlterField(
            model_name='chessboard',
            name='weightKg',
            field=models.FloatField(default=1.0),
        ),
    ]
