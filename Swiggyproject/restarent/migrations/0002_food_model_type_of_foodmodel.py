# Generated by Django 3.0 on 2020-05-03 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restarent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_of_foodmodel',
            fields=[
                ('Food_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Food_Type', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food_model',
            fields=[
                ('Food_Name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Food_price', models.FloatField()),
                ('Food_Image', models.ImageField(upload_to='foods/')),
                ('Food_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restarent.Type_of_foodmodel')),
            ],
        ),
    ]
