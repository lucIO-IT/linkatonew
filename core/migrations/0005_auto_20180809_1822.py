# Generated by Django 2.0.7 on 2018-08-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180805_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='corso',
            name='obiettivi_corso',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='corso',
            name='programma_corso',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
    ]
