# Generated by Django 3.2 on 2021-08-24 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP', '0002_auto_20210424_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacaIngresando',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.JSONField()),
            ],
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='posicion',
            field=models.CharField(default='---', max_length=5),
        ),
    ]
