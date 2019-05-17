# Generated by Django 2.0.7 on 2018-08-24 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_lezione_data_lezione'),
        ('index', '0002_auto_20180812_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='utente',
            name='preferiti',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Corso'),
        ),
        migrations.AlterField(
            model_name='utente',
            name='scuola',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
