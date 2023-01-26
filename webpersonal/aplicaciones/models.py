from django.db import models
# Create your models here.

class Portafolio(models.Model):
    titulo= models.CharField(max_length=200,null=False,) #verbose_name = "por si queremos cambiar el nombre del campo"
    rol= models.CharField(max_length=200,null=False)
    tecnologia = models.CharField(max_length=200)   
    descripción=models.TextField(null=False)
    imagen=models.ImageField(null=False,upload_to="portafolio") #upload_to="portafolio") crea dentro de media un dir portafolio y aloja las img ahí
    created=models.DateTimeField(auto_now_add=True)  #fecha de creación
    updated=models.DateTimeField(auto_now=True) #Fecha de actualización

    #Devuelve el nombre del proyecto en /admin
    def __str__(self):
        return self.titulo

class Meta:
        #ordenar por fecha de creación
    ordenring = ["-created"]
    
    
