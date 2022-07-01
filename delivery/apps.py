from django.apps import AppConfig


class DeliveryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'delivery'


class UserConfig(AppConfig):
    name = 'users'
    def ready(self):
        import users.signals


