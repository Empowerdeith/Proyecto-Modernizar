from django.db import models


class Reglamento(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    archivo = models.FileField(upload_to='uploads/reglamento/')

    def __str__(self):
        return self.nombre

        
class ToolsLeft(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    utilesCurso = models.FileField(upload_to='uploads/tools/')

    class Meta:
        verbose_name = "Utiles Izquierda"
        verbose_name_plural = "Utiles Barra Izquierda"

    def __str__(self):
        return self.nombre

   
class ToolsCenter(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    utilesCurso = models.FileField(upload_to='uploads/tools/')

    class Meta:
        verbose_name = "Utiles Centro"
        verbose_name_plural = "Utiles Barra Central"

    def __str__(self):
        return self.nombre

  
class ToolsRight(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    utilesCurso = models.FileField(upload_to='uploads/tools/')

    class Meta:
        verbose_name = "Utiles Derecha"
        verbose_name_plural = "Utiles Barra Derecha"

    def __str__(self):
        return self.nombre
