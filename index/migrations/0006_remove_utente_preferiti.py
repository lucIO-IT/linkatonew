# Generated by Django 2.0.7 on 2018-08-24 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_utente_preferiti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utente',
            name='preferiti',
        ),
    ]