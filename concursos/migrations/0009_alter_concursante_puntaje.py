# Generated by Django 4.1 on 2022-08-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concursos', '0008_remove_calificacion_acordeonero_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concursante',
            name='puntaje',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Puntaje'),
        ),
    ]
