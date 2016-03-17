import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

import django
django.setup()

from personas.models import Character, Relationship, Organization, Membership, Skill, Location, Nation


NATION = Nation.objects.get(pk=1)
LOCATION = Location.objects.get(pk=2)

'''CHARACTER_DICT = {"Marcus Calius": ["Marcus Calius","Protagonist", 79, 
    "Legionnaire and priest of Jupiter", 25, NATION, LOCATION, LOCATION, [
    ("Athletics", 8, "General"),
    ("Archery", 4, "General"),
    ("Favour (Jupiter)", 10, "General")
    ]],
    "Feargus Nerviorum": ["Feargus Nerviorum", "Progatonist", 79,
    "Celtic scout in the legions of Rome", 27, NATION, LOCATION, LOCATION, [
    ("Athletics", 7, "General"),
    ("Survival", 2, "Investigative")
    ]],
    "Celt Warrior": ["Celt Warrior", "Antagonist", 0, "A hardened and courageous warrior of the Celts", 
    23, NATION, LOCATION, LOCATION, [
    ("Threat", 4, "General"),
    ("Attack", 5, "General"),
    ("Defense", 4, "General"),
    ("Mental Def", 4, "General"),
    ("Physical Def", 4, "General"),
    ("Sense", 3, "General"),
    ("Sneak", 4, "General"),
    ("Move", 4, "General"),
    ("Pool", 6, "General"),
    ]]}'''

SKILL_LIST = ('allies', 'archery', 'burglary', 'favour', 'gambling', 
        'healing', 'health', 'legerdemain', 'preparedness', 'pugilism', 
        'riding', 'sailing', 'sense_trouble', 'solace', 'stability', 
        'stealth','traps', 'wealth', 'weapons')

INVESTIGATIVE_SKILL_LIST = ('Cunning','Appraise','Local Area','Battle',
    'Craft','Notice','Perform', 'Profession', 'Scout','Interpersonal',
    'Bargaining','Bureacracy','Charm', 'Diplomacy', 'High Society',
    'Inspiration', 'Intimidate', 'Military Lingo','Reputation (rep)',
    'Sense Motive','Streetwise','Tradecraft','Lore','Alchemy','Arcana',
    'Beasts','Culture', 'Dungeoneering', 'Engineering', 'Geography', 'History',
    'Linguistics', 'Medicine', 'Nature', 'Occultism','Omens','Politics','Religion')


def populate():

    for character in CHARACTER_DICT:
        print(CHARACTER_DICT[character])
        (name, c_type, xp, description, age, nationality, birthplace, base_of_operations, skills) = CHARACTER_DICT[character]
        add_character(name, c_type, xp, description, age, nationality, birthplace, base_of_operations)
        
        c = Character.objects.get(name=name)

        print(skills)
        for skill in skills:
            (name, value, s_type) = skill
            add_skill(c, name, value, s_type)

    '''for skill in SKILL_LIST:
        add_skill(skill.title(), 10, "General")

    for skill in INVESTIGATIVE_SKILL_LIST:
        add_skill(skill.title(), 1, "Investigative")'''

def add_skill(character, name, value, s_type, *args, **kwargs):
    s = Skill.objects.get_or_create(name=name, value=value, s_type=s_type, character=character)
    return s

def add_character(name, c_type, xp, description, age, nationality, birthplace, base_of_operations, *args, **kwargs):
    user = User.objects.get(pk=1)
    c = Character.objects.get_or_create(name=name, c_type=c_type, xp=xp, description=description,
        nationality=nationality, birthplace=birthplace, base_of_operations=base_of_operations, creator=user, slug=(slugify(name)))
    return c

# Start execution here
if __name__ == '__main__':
    print('Starting population script')
    populate()
