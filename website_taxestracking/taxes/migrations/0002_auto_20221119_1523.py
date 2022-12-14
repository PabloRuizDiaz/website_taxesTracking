# Generated by Django 3.2.2 on 2022-11-19 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='taxNameModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, choices=[('muni', 'Impuestos Municipales'), ('prov', 'Impuestos Provinciales'), ('naci', 'Impuestos Nacionales'), ('sepu', 'Servicios Publicos'), ('sepr', 'Servicios Privados')], max_length=4, null=True)),
                ('tax', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'tax_name',
            },
        ),
        migrations.RemoveField(
            model_name='taxesmodel',
            name='category',
        ),
        migrations.AlterField(
            model_name='taxesmodel',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='taxes.taxnamemodel'),
        ),
    ]
