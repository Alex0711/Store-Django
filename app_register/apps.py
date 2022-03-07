from django.apps import AppConfig


class AppRegisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_register'

    def ready(self):
        import app_register.signals