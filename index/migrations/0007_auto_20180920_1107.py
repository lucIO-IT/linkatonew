# Generated by Django 2.0.7 on 2018-09-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_remove_utente_preferiti'),
    ]

    operations = [
        migrations.AddField(
            model_name='utente',
            name='provincia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='utente',
            name='regione',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='utente',
            name='scuola',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Codice Mecanografico'),
        ),
    ]
