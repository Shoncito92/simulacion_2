# Generated by Django 3.1.7 on 2021-03-13 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_auto_20210313_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estadocivil',
            old_name='nameEC',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='genero',
            old_name='nameGE',
            new_name='name',
        ),
    ]
