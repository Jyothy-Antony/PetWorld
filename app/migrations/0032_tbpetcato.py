# Generated by Django 2.0.7 on 2018-09-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_delete_tbpetcato'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbpetcato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cato', models.CharField(max_length=100)),
                ('petcatoimg', models.ImageField(blank=True, null=True, upload_to='Images/pettype', verbose_name='file')),
            ],
        ),
    ]
