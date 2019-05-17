# Generated by Django 2.0.7 on 2019-01-06 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0020_auto_20190106_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Risorsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('contenuto', models.ForeignKey(limit_choices_to={'model__in': ('filepdf', 'linkvideo')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('corso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corso', to='core.Corso')),
            ],
            options={
                'verbose_name': 'Risorsa',
                'verbose_name_plural': 'Risorse',
            },
        ),
    ]
