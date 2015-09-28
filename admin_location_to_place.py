import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

import django
django.setup()

from personas.models import StoryObject, Place, Relationship, Location, Nation, Note


def transform():

    locations = Location.objects.all()

    for location in locations:
        p = Place.objects.get_or_create(
            name=location.name,
            creator=location.creator,
            c_type="Place",
            role=location.terrain,
            description="{}\nFeatures: {}".format(location.description,
                location.features),
            nationality=location.nation,
            latitude=location.latitude,
            longitude=location.longitude,
            image=location.image,
            story=location.story,
            published=location.published,
            slug=slugify("{}-{}".format(location.story.title, location.name)))

        print("Tranformed location {}".format(location.name))

        notes = Note.objects.filter(location=location)

        if notes:

            for note in notes:
                note.storyobject = StoryObject.objects.get(name=location.name)
                note.location = None
                note.save()
                print("Updated note {}".format(note.title))


    print("***Finished converting locations***\n")
    storyobjects = StoryObject.objects.exclude(c_type="Place")

    print("***Starting to add relationships***\n")
    for storyobject in storyobjects:
        if storyobject.base_of_operations is not None:
            try:
                r = Relationship.objects.get_or_create(
                    from_storyobject=storyobject,
                    to_storyobject__name=storyobject.base_of_operations.name,
                    relationship_class="Operates out of",
                    weight=5,
                    relationship_description="Home base")
                print("created relationship between {} and {}".format(storyobject.name, storyobject.base_of_operations))
            except StoryObject.DoesNotExist:
                pass
        else:
            print("No base for {}".format(storyobject.name))
            print(storyobject.base_of_operations)

    scenes = Scene.objects.all()

    for scene in scenes:
        scene.place = Place.objects.get(name=scene.location.name)
        scene.save()
        print("Updated scene {}".format(scene.title))

# Start execution here
if __name__ == '__main__':
    print('Starting population script')
    transform()
