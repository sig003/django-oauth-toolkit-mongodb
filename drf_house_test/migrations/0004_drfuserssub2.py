# Generated by Django 4.1 on 2022-10-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_house_test', '0003_drfuserssub'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrfUsersSub2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.UUIDField()),
                ('test', models.CharField(max_length=256)),
            ],
        ),
    ]
