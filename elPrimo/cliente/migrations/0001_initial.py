# Generated by Django 4.2 on 2023-05-21 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('correo', models.EmailField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Info_Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=50)),
                ('urbanizacion', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(max_length=12, unique=True)),
                ('direccion', models.TextField(max_length=150)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.usuario')),
            ],
        ),
    ]