# Generated by Django 2.0.7 on 2018-08-01 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_tbboarlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbcontact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('msg', models.CharField(max_length=1000)),
            ],
        ),
    ]
