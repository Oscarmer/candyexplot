# Generated by Django 4.0.3 on 2022-07-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candyapp', '0018_remove_historial_fz_fz_id_finanza_id_hs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial_fz',
            name='costot',
            field=models.IntegerField(null=True, verbose_name='Costo total'),
        ),
    ]