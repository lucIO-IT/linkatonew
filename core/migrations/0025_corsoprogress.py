# Generated by Django 2.0.7 on 2019-05-18 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0024_auto_20190516_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorsoProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corsi', to='core.Corso')),
                ('studente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Progresso Studenti',
                'verbose_name_plural': 'Progresso Studenti',
            },
        ),
    ]
