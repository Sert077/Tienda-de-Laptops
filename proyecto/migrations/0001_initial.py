# Generated by Django 4.1.7 on 2023-03-31 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20, unique=True)),
                ('modelo', models.CharField(max_length=20, unique=True)),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('pantalla', models.FloatField()),
                ('teclado', models.CharField(max_length=10, unique=True)),
                ('procesador', models.CharField(max_length=25, unique=True)),
                ('ram', models.IntegerField()),
                ('color', models.CharField(max_length=15, unique=True)),
                ('m2', models.IntegerField()),
                ('hdd', models.IntegerField()),
                ('grafica', models.CharField(max_length=25, unique=True)),
                ('descrip', models.CharField(max_length=300, unique=True)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/productos')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.project')),
            ],
        ),
    ]
