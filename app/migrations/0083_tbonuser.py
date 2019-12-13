# Generated by Django 2.1.3 on 2018-11-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0082_delete_tbonuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbonuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usersid', models.IntegerField()),
                ('varid', models.IntegerField()),
                ('date', models.CharField(max_length=100)),
                ('petid', models.IntegerField()),
                ('repdate', models.CharField(max_length=100)),
                ('descriptions', models.CharField(max_length=50000)),
                ('desclastupdate', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('useracc', models.CharField(max_length=100)),
                ('dateuseracc', models.CharField(max_length=100)),
                ('handler', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('days', models.CharField(max_length=100)),
            ],
        ),
    ]