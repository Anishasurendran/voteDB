# Generated by Django 3.0.3 on 2020-03-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_auto_20200320_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='election_name',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
