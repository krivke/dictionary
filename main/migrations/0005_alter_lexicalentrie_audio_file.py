# Generated by Django 3.2.6 on 2021-08-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_lexicalentrie_phonetic_spelling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lexicalentrie',
            name='audio_file',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
