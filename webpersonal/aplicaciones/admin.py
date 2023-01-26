from django.contrib import admin
from .models import Portafolio

# Register your models here.

#clase para extender la funcionalidad del Admin
#Para ver la fecha y hora de creacion y actualización
#En solo lectura.

class ProjectAdmin (admin.ModelAdmin):
    readonly_fields = ('created','updated')


admin.site.register(Portafolio,ProjectAdmin)
