from django.db import models


class Reglamento(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    archivo = models.FileField(upload_to='media/uploads/reglamento/')

    def __str__(self):
        return self.nombre


class Cursos(models.Model):
    curso = models.CharField(max_length=150, null=False, blank=False)
    utilesCurso = models.FileField(upload_to='media/uploads/cursos/')

    class Meta:
        verbose_name = "Cursos"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.curso
