# Generated by Django 3.0.2 on 2020-01-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authenticate_vote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='adhar_number',
            field=models.IntegerField(default=0),
        ),
    ]
