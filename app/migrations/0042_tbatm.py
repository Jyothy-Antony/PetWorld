# Generated by Django 2.0.7 on 2018-09-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_tbpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbatm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Atmno', models.CharField(max_length=12)),
                ('amt', models.CharField(max_length=15)),
                ('expm', models.CharField(max_length=2)),
                ('expy', models.CharField(max_length=4)),
            ],
        ),
    ]