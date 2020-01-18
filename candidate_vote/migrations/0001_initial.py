# Generated by Django 3.0.2 on 2020-01-18 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(default=None, max_length=15)),
                ('cand_address', models.CharField(default=None, max_length=30)),
                ('cand_gender', models.CharField(default=None, max_length=10)),
                ('cand_district', models.CharField(default=None, max_length=10)),
                ('cand_taluk', models.CharField(default=None, max_length=10)),
                ('cand_phoneno', models.IntegerField(default=0, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_sdate', models.DateField(default=None)),
                ('election_edate', models.DateField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Electioninfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate_vote.CandidateDetails')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate_vote.Election')),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=0)),
                ('elect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate_vote.Electioninfo')),
            ],
        ),
    ]
