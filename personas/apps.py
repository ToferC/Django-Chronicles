from django.apps import AppConfig
import os
import watson

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class PersonasConfig(AppConfig):
    name = 'personas'
    verbose_name = "Personas"
    path = os.path.join(BASE_DIR,)

    def ready(self):
        StoryObject = self.get_model("StoryObject")
        watson.register(StoryObject)
        Location = self.get_model("Location")
        watson.register(Location)
        Nation = self.get_model("Nation")
        watson.register(Nation)
        Story = self.get_model("Story")
        watson.register(Story)
        Chapter = self.get_model("Chapter")
        watson.register(Chapter)
        Scene = self.get_model("Scene")
        watson.register(Scene)
