# Generated by Django 4.1 on 2022-10-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_house_test', '0007_tabletest_delete_useridtest'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.UUIDField(editable=False)),
                ('test', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'user_table_name',
            },
        ),
    ]
