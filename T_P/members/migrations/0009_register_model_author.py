# Generated by Django 3.1.4 on 2020-12-14 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_remove_register_model_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_model',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.author'),
            preserve_default=False,
        ),
    ]
