# Generated by Django 3.2.11 on 2022-01-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotapp', '0002_don_sm'),
    ]

    operations = [
        migrations.AddField(
            model_name='don',
            name='p',
            field=models.IntegerField(null=True),
        ),
    ]
