# Generated by Django 4.2.6 on 2023-10-16 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_alter_cursos_utilescurso_alter_reglamento_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='utilesCurso',
            field=models.FileField(upload_to='uploads/cursos/'),
        ),
        migrations.AlterField(
            model_name='reglamento',
            name='archivo',
            field=models.FileField(upload_to='uploads/reglamento/'),
        ),
    ]
