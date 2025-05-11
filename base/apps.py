"""App configuration for base app."""

from django.apps import AppConfig

class BaseConfig(AppConfig):
    """
        Configuration class for the base app.
        Sets the default auto field and app name for the base application.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "base"
