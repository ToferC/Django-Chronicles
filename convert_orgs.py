import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

import django
django.setup()

from personas.models import Organization, StoryObject, Membership, Relationship


s = StoryObject.objects.all()

for i in s:
    if i.c_type not in "Character Thing Force Organization Creature":
        i.c_type = "Character"
        i.save()
        print(i)

print("StoryObjects converted")

'''o = Organization.objects.all()

for i in o:
    s = StoryObject(
        name = i.name,
        creator = i.creator,
        c_type = "Organization",
        role = i.purpose,
        description = i.description,
        nationality = i.location.nation,
        base_of_operations = i.location,
        image = i.image,
        slug = i.slug,
        stats_toggle = True,
        skill_toggle = True,
        combat_toggle = True,
        gallery_toggle = True,
        social_toggle = True,
        )
    s.save()'''



''' Organization
    name = models.CharField(max_length=128)
    creator = models.ForeignKey(User, blank=True, null=True)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(StoryObject, through='Membership', blank=True)
    purpose = models.CharField(max_length=128)
    region = models.CharField(max_length=128)
    location = models.ForeignKey(Location)
    story = models.ForeignKey('Story')
    image = models.ImageField(upload_to='organization_images/%Y/%m/%d', default='organization_images/nothing.jpg')

    slug = models.SlugField(unique=True) '''

''' StoryObject
creator = models.ForeignKey(User, unique=False, blank=True)
    name = models.CharField(max_length=128, unique=False)
    story = models.ForeignKey('Story', default=1)
    c_type = models.CharField(choices=CHAR_CHOICES, 
        max_length=32, default="Character", verbose_name="Story Object Type",
        help_text="Select a story object category.")
    role = models.CharField(max_length=256)
    description = MarkdownField(blank=True)
    nationality = models.ForeignKey(Nation, blank=True, null=True)
    base_of_operations = models.ForeignKey(Location, related_name='active_in', 
        blank=True, null=True )

    image = models.ImageField(
        upload_to='profile_images/%Y/%m/%d/%H/%M/%S', default='profile_images/shadow_figure.jpeg')
    slug = models.SlugField(unique=True) '''

