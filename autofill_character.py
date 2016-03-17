import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

import django
django.setup()

from personas.models import StoryObject, Statistic, Skill, Ability, Aspect, CombatInfo

s = StoryObject.objects.get(name="Helios")

role = "Level 1 Fighter"

stats = "Strength Dexterity Constitution Intelligence Wisdom Charisma".split()

for i in stats:
    x = Statistic(name=i, value=10, stat_type="Type_1", storyobject=s)
    x.save()
    print(x)

derived_stats = "AC HP MV Attacks".split()
ds_values = {"AC":4, "HP":6, "MV":30, "Attacks":1}

for k, v in ds_values.items():
    x = Statistic(name=k, value=v, stat_type="Type_2", storyobject=s)
    x.save()
    print(x)

print("StoryObjects converted")
