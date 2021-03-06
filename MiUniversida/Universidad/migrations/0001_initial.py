# Generated by Django 3.2.5 on 2021-12-11 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('matricula', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
