# Generated by Django 4.2.6 on 2023-11-15 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abandonados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=30)),
                ('año_publicacion', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Leidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=30)),
                ('año_publicacion', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Leyendo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=30)),
                ('año_publicacion', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Por_Leer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=30)),
                ('año_publicacion', models.CharField(max_length=4)),
            ],
        ),
    ]
