# Generated by Django 3.1.4 on 2020-12-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20201212_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_P_Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Designation', models.CharField(max_length=50)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Ph_number', models.CharField(max_length=12)),
            ],
        ),
    ]
