from django.apps import AppConfig
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class PersonasConfig(AppConfig):
    name = 'personas'
    verbose_name = "Personas"
    path = os.path.join(BASE_DIR,)
