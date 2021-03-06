# Generated by Django 3.0 on 2020-04-16 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s_adminapp', '0002_statemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('City_No', models.AutoField(primary_key=True, serialize=False)),
                ('City_Name', models.CharField(max_length=40, unique=True)),
                ('State_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_adminapp.StateModel')),
            ],
        ),
        migrations.CreateModel(
            name='AreaModel',
            fields=[
                ('Area_No', models.AutoField(primary_key=True, serialize=False)),
                ('Area_Name', models.CharField(max_length=30, unique=True)),
                ('City_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_adminapp.CityModel')),
            ],
        ),
    ]
