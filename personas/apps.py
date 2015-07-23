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
        watson.register(StoryObject.objects.filter(published=True))
        Location = self.get_model("Location")
        watson.register(Location.objects.filter(published=True))
        Nation = self.get_model("Nation")
        watson.register(Nation.objects.filter(published=True))
        Story = self.get_model("Story")
        watson.register(Story.objects.filter(published=True))
        Chapter = self.get_model("Chapter")
        watson.register(Chapter.objects.filter(published=True))
        Scene = self.get_model("Scene")
        watson.register(Scene.objects.filter(published=True))
        Note = self.get_model("Note")
        watson.register(Note.objects.all())
