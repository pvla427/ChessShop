# Generated by Django 3.2.9 on 2021-12-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211226_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='experience',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='firstName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='lastName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='patronymic',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
