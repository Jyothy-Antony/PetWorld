# Generated by Django 2.1.3 on 2018-11-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0076_delete_tbshoping'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbshoping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('cato', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('quty', models.CharField(max_length=100)),
                ('expdate', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Images/petdocs', verbose_name='file')),
            ],
        ),
    ]