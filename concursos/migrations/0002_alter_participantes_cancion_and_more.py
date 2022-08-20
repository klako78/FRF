# Generated by Django 4.1 on 2022-08-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantes',
            name='cancion',
            field=models.CharField(max_length=100, verbose_name='Nombre de la cancion'),
        ),
        migrations.AlterField(
            model_name='participantes',
            name='categoria',
            field=models.CharField(choices=[('CANCION INEDITA', 'Cnacion inedita'), ('ACORDEONERO', 'Acordeonero'), ('PIQUERIA', 'Piqueria')], max_length=100, verbose_name='Tipo Medida'),
        ),
        migrations.AlterField(
            model_name='participantes',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]