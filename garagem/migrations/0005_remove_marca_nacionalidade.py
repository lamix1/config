# Generated by Django 4.2.4 on 2023-08-22 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0004_alter_acessorio_options_alter_cor_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marca',
            name='nacionalidade',
        ),
    ]
