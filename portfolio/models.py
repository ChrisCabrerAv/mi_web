from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen")
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Última actualización", auto_now=True)

    class Meta:
        verbose_name = "proyecto"
        ordering = ['-created']