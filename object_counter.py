import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
from django.contrib.auth.models import User
from django.db.models import F
from django.template.defaultfilters import slugify

import django
django.setup()

from personas.models import Story, StoryObject, Nation, Chapter, Scene, Location


s = Story.objects.all()

for story in s:
    counter = 0
    counter += StoryObject.objects.filter(story=story).count()
    counter += Nation.objects.filter(story=story).count()
    counter += Chapter.objects.filter(story=story).count()
    counter += Scene.objects.filter(chapter__story=story).count()
    counter += Location.objects.filter(story=story).count()

    print(story.title, counter)

    story.object_count = F('object_count') + counter
    story.save()

print("StoryObjects counted")