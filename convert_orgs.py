import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

import django
django.setup()

from personas.models import StoryObject, Relationship, Nation

n = Nation.objects.all()

print("Starting to convert nations to StoryObjects\n")

for i in n:
    s = StoryObject.objects.update_or_create(
        name = i.name,
        creator = i.creator,
        story = i.story,
        c_type = "Faction",
        role = "Faction",
        description = i.description,
        image = i.image,
        slug = slugify("{}-{}".format(i.story.title, i.name)),
        published = i.published,
        )
    print("{} is converted to a Faction".format(i.name))

s = StoryObject.objects.all()

for i in s:
    if i.c_type == "Force":
        i.c_type = "Faction"
        i.save()
        print(i)

print("StoryObjects converted\n")

print("Starting to convert nationalities to relationship")

for i in s:
    if i.nationality:
        r = Relationship(
            from_storyobject = i,
            to_storyobject = StoryObject.objects.filter(name=i.nationality.name).first(),
            if i.c_type in  "Place Organization Creature Thing":
                elationship_class = "Located in"
            else:
                relationship_class = "Citizen of",
            relationship_description = "Default",
            weight = 5)
        r.save()
        print("Added relationship from {} to {}".format(
            i, i.nationality))

print("Finished execution")