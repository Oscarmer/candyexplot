# Generated by Django 4.0.3 on 2022-07-02 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candyapp', '0012_compt_lg_finanza_lg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compt',
            old_name='lg',
            new_name='id_lg',
        ),
        migrations.RenameField(
            model_name='finanza',
            old_name='lg',
            new_name='id_lg',
        ),
    ]