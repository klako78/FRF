# Generated by Django 4.1 on 2022-08-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concursos', '0009_alter_concursante_puntaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concursante',
            name='ronda',
            field=models.CharField(default='1', max_length=100, verbose_name='Ronda'),
        ),
    ]