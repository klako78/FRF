# Generated by Django 4.1 on 2022-08-15 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concursos', '0006_alter_concursante_puntaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concursante',
            name='puntaje',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Puntaje'),
            preserve_default=False,
        ),
    ]