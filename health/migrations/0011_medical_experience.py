# Generated by Django 3.1.4 on 2020-12-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0010_auto_20201224_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='medical',
            name='experience',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
