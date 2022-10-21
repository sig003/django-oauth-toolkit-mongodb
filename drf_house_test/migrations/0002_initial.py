# Generated by Django 4.1 on 2022-10-20 07:17

from django.db import migrations, models
import djongo.models.fields
import drf_house_test.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('house', djongo.models.fields.ArrayField(model_container=drf_house_test.models.House)),
            ],
        ),
    ]
