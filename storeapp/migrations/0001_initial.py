# Generated by Django 5.1.4 on 2024-12-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_id', models.IntegerField(default=None)),
                ('latitude', models.FloatField(default=None)),
                ('longitude', models.FloatField(default=None)),
                ('availability_radius', models.FloatField(default=None)),
                ('open_hour', models.TimeField(default=None)),
                ('close_hour', models.TimeField(default=None)),
                ('rating', models.FloatField(default=None)),
            ],
        ),
    ]
