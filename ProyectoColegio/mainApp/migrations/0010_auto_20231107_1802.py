# Generated by Django 3.1.2 on 2023-11-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_auto_20231107_1459'),
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
