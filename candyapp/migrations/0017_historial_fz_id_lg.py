# Generated by Django 4.0.3 on 2022-07-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candyapp', '0016_historial_fz_costot'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial_fz',
            name='id_lg',
            field=models.IntegerField(default=1, verbose_name='Lugar'),
            preserve_default=False,
        ),
    ]
