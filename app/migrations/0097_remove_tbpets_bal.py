# Generated by Django 2.0.6 on 2019-01-04 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0096_auto_20190102_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbpets',
            name='bal',
        ),
    ]