# Generated by Django 4.2 on 2023-06-04 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('tienda', '0004_alter_encabezado_factura_direccion_despacho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encabezado_factura',
            name='direccion_despacho',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.info_usuario'),
        ),
    ]
