from django.apps import AppConfig

class BaseConfig(AppConfig):
    name = 'delivery'

    def ready(self):
        import delivery.signals