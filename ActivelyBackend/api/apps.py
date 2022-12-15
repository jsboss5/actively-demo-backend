from django.apps import AppConfig


class QuickstartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    def ready(self):
        print("test")