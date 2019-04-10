# Generated by Django 2.0.7 on 2018-08-04 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lezione',
            name='data_lezione',
        ),
        migrations.AddField(
            model_name='corso',
            name='data_corso',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]