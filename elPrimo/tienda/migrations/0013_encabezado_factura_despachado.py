# Generated by Django 4.2 on 2023-06-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0012_encabezado_factura_dolar'),
    ]

    operations = [
        migrations.AddField(
            model_name='encabezado_factura',
            name='despachado',
            field=models.BooleanField(default=False),
        ),
    ]
