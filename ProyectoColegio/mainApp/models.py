from django.db import models


class Reglamento(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    archivo = models.FileField(upload_to='uploads/reglamento/')

    def __str__(self):
        return self.nombre


"""class Cursos(models.Model):
    curso = models.CharField(max_length=150, null=False, blank=False)
    utilesCurso = models.FileField(upload_to='uploads/cursos/')

    class Meta:
        verbose_name = "Cursos"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.curso"""
    
class NivTransicion(models.Model):
    nivtransicion = models.CharField(max_length=150, null=False, blank=False)
    utilesCurso = models.FileField(upload_to='uploads/nivtransicion/')

    class Meta:
        verbose_name = "NivTransicion"
        verbose_name_plural = "Nivel de Transición"

    def __str__(self):
        return self.nivtransicion

class EdBasica(models.Model):
    edbasica = models.CharField(max_length=150, null=False, blank=False)
    utilesCurso = models.FileField(upload_to='uploads/edbasica/')

    class Meta:
        verbose_name = "EdBasica"
        verbose_name_plural = "Enseñanza Básica"

    def __str__(self):
        return self.edbasica
