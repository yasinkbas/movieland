# Generated by Django 2.2.4 on 2019-08-11 20:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('imdb', models.FloatField(validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
    ]