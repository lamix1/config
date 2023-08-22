# Generated by Django 4.2.4 on 2023-08-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('garagem', '0002_veiculo_capa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='capa',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='capa',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='+', to='uploader.image'),
        ),
    ]