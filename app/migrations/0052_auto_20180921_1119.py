# Generated by Django 2.0.7 on 2018-09-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_tbhandlers'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbhandlers',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Images/licence', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='tbhandlers',
            name='tlicence',
            field=models.ImageField(blank=True, null=True, upload_to='Images/licence', verbose_name='file'),
        ),
    ]
