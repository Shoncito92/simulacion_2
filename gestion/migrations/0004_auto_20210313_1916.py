# Generated by Django 3.1.7 on 2021-03-13 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20210313_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='direccion_calle',
            new_name='calle',
        ),
        migrations.RenameField(
            model_name='perfil',
            old_name='direccion_numero',
            new_name='numero_casa',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='estado_civil',
        ),
        migrations.AddField(
            model_name='perfil',
            name='estado_civil',
            field=models.ManyToManyField(help_text='Seleccione Estado Civil', to='gestion.EstadoCivil'),
        ),
    ]