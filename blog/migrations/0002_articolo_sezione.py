# Generated by Django 2.0.7 on 2018-08-10 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articolo',
            name='sezione',
            field=models.CharField(blank=True, choices=[('1', 'Chi siamo'), ('2', 'Per le aziende'), ('3', 'top_new'), ('4', 'card_sx'), ('5', 'card_cc'), ('6', 'card_dx')], max_length=1, null=True),
        ),
    ]