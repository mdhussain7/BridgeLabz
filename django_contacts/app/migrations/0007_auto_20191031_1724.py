# Generated by Django 2.2.6 on 2019-10-31 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20191031_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
