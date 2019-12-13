# Generated by Django 2.1.3 on 2018-11-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0090_delete_chart'),
    ]

    operations = [
        migrations.CreateModel(
            name='chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petid', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('bordid', models.IntegerField()),
                ('month', models.CharField(max_length=100)),
                ('vaccname', models.CharField(max_length=100)),
                ('cvdate', models.CharField(max_length=100)),
                ('expense', models.CharField(max_length=100)),
                ('totalamount', models.CharField(max_length=100)),
            ],
        ),
    ]
