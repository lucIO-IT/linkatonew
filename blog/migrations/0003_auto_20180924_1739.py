# Generated by Django 2.0.7 on 2018-09-24 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_articolo_sezione'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articolo',
            options={'verbose_name': 'Articolo', 'verbose_name_plural': 'Articoli'},
        ),
    ]