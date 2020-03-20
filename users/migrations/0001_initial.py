# Generated by Django 3.0.3 on 2020-03-20 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_number', models.CharField(default=None, max_length=12)),
                ('name', models.CharField(default=None, max_length=10)),
                ('address', models.CharField(default=None, max_length=30)),
                ('careof', models.CharField(default=None, max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('dob', models.DateField(default=None)),
                ('district', models.CharField(default=None, max_length=15)),
                ('phone_number', models.CharField(default=None, max_length=10)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('face_encodings', models.BinaryField(null=True)),
                ('location', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='election.Location')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]