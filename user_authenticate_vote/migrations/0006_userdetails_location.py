# Generated by Django 3.0.2 on 2020-02-01 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_vote', '0004_auto_20200201_1402'),
        ('user_authenticate_vote', '0005_merge_20200127_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='candidate_vote.Location'),
        ),
    ]