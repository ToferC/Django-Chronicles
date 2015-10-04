import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.base import ObjectDoesNotExist


import django
django.setup()

from personas.models import StoryObject, Relationship, Nation

n = Nation.objects.all()

print("Starting to convert nations to StoryObjects\n")

for i in n:

    print("Trying to convert {}".format(i.name))

    try:
        so = StoryObject.objects.filter(name=i.name)
    except ObjectDoesNotExist:
        so = None

    if so:
        pass
    else:
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

    try:
        notes = Note.objects.filter(nation=n)
    except KeyError:
        pass

    if notes:

        for note in notes:
            note.storyobject = StoryObject.objects.get(name=n.name)
            note.nation = None
            note.save()
            print("Updated note {}".format(note.title))


print("Starting to convert existing story objects from Force to Faction.")
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

        if i.c_type in  "Place Organization Creature Thing":
            insert_RC = "Located in"
        else:
            insert_RC = "Citizen of"

        r = Relationship(
            from_storyobject = i,
            to_storyobject = StoryObject.objects.filter(name=i.nationality.name).first(),
            relationship_class = insert_RC,
            relationship_description = "Default",
            weight = 5)
        r.save()
        print("Added relationship from {} to {}".format(
            i, i.nationality))


print("Finished execution")