# Generated by Django 3.2.6 on 2021-08-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lexicalentrie',
            name='audio_file',
            field=models.CharField(max_length=300),
        ),
    ]
