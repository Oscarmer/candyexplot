# Generated by Django 4.0.3 on 2022-07-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candyapp', '0022_alter_historial_fz_costot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armado',
            name='precio',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='candycarrito',
            name='precio',
            field=models.FloatField(null=True, verbose_name='precio'),
        ),
        migrations.AlterField(
            model_name='entregado',
            name='precio',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='entregado',
            name='preciot',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='finanza',
            name='costot',
            field=models.FloatField(null=True, verbose_name='Costo total'),
        ),
        migrations.AlterField(
            model_name='infofactura',
            name='precio',
            field=models.FloatField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='mezcla',
            name='costo',
            field=models.FloatField(verbose_name='costo'),
        ),
        migrations.AlterField(
            model_name='posicion',
            name='precio',
            field=models.FloatField(verbose_name='precio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(verbose_name='Precio base'),
        ),
    ]
