from django.apps import AppConfig


class AplicacionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicaciones'
    verbose_name = 'Gestión'

    class Meta:
        #ordenar por fecha de creación
        orden = ["-created"]
    
    def __str__(self):
        return self.titulo
