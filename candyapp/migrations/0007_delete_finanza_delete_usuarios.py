# Generated by Django 4.0.3 on 2022-07-02 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candyapp', '0006_alter_materia_p_costo_alter_materia_p_costo_u'),
    ]

    operations = [
        migrations.DeleteModel(
            name='finanza',
        ),
        migrations.DeleteModel(
            name='usuarios',
        ),
    ]
