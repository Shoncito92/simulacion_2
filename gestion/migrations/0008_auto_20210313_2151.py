# Generated by Django 3.1.7 on 2021-03-14 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_remove_perfil_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='rol',
            field=models.ForeignKey(default='Ingrese un breve descripcion', on_delete=django.db.models.deletion.CASCADE, to='gestion.rol'),
        ),
    ]