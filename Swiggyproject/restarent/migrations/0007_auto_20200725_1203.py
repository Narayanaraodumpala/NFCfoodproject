# Generated by Django 3.0 on 2020-07-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restarent', '0006_auto_20200717_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileSessionModel',
            fields=[
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=7)),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=16)),
                ('Door_No', models.CharField(max_length=10)),
                ('Street', models.CharField(max_length=30)),
                ('Area_Or_Village', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Profileseiion',
        ),
    ]
