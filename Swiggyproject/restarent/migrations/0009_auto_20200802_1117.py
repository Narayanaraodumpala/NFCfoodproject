# Generated by Django 3.0 on 2020-08-02 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restarent', '0008_auto_20200726_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='profile',
            field=models.CharField(default=None, max_length=2, primary_key=True, serialize=False),
        ),
    ]