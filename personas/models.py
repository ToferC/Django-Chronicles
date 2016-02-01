from django.db import models
from django.db.models import F
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django_markdown.models import MarkdownField
from personas.personas_email import mail_format as mail_format
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Aspect(models.Model):
    CORE = "CO"
    VALUES = "VA"
    BACKGROUND = "BA"
    FLAW = "FL"

    ASPECT_TYPE_CHOICES = (
        (CORE, "Core"),
        (VALUES, "Values"),
        (BACKGROUND, "Background"),
        (FLAW, "Flaw")
        )

    label = models.CharField(max_length=12, choices=ASPECT_TYPE_CHOICES, default="CO", blank=True)
    name = models.CharField(max_length=128)
    details = models.TextField(blank=True, null=True, help_text="Enter any additional details about your aspect here.")
    storyobject = models.ForeignKey('StoryObject')

    def save(self, *args, **kwargs):
        super(Aspect, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


class Ability(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    storyobject = models.ForeignKey('StoryObject', null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Ability, self).save(*args, **kwargs)


    def __str__(self):
        return "{}: {}".format(self.name, self.description)


class Note(models.Model):
    creator = models.ForeignKey(User, default=0)
    content = MarkdownField(blank=True)
    title = models.CharField(max_length=32, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    storyobject = models.ForeignKey("StoryObject", blank=True, null=True)
    place = models.ForeignKey("Place", blank=True, null=True, related_name="loc2note")
    scene = models.ForeignKey("Scene", blank=True, null=True)
    chapter = models.ForeignKey("Chapter", blank=True, null=True)
    story = models.ForeignKey("Story", blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return self.content


class GalleryImage(models.Model):
    creator = models.ForeignKey(User)
    image = models.ImageField(upload_to='content_images/%Y/%m/%d/%H_%M_%S', default='content_images/nothing.jpg')
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now=True)
    storyobject = models.ForeignKey("StoryObject", blank=True, null=True)
    place = models.ForeignKey("Place", blank=True, null=True, related_name="loc2image")
    scene = models.ForeignKey("Scene", blank=True, null=True)
    chapter = models.ForeignKey("Chapter", blank=True, null=True)
    story = models.ForeignKey("Story", blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        super(GalleryImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ScratchPad(models.Model):
    creator = models.ForeignKey(User, default=0)
    content = MarkdownField(blank=True)
    date = models.DateTimeField(auto_now=True)
    storyobject = models.ForeignKey("StoryObject", blank=True, null=True)

    def __str__(self):
        return self.content


class Equipment(models.Model):
    creator = models.ForeignKey(User, default=0)
    content = MarkdownField(blank=True, default="Enter your equipment here.")
    date = models.DateTimeField(auto_now=True)
    storyobject = models.ForeignKey("StoryObject", blank=True, null=True)

    def __str__(self):
        return self.content


class Communique(models.Model):
    author = models.ForeignKey("StoryObject", related_name="Author")
    receiver = models.ForeignKey("StoryObject", related_name="Receiver")
    date = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=140)
    rating = models.PositiveSmallIntegerField(default=0)

    def save(self, author, *args, **kwargs):
        self.author = author
        super(Communique, self).save(*args, **kwargs)

    def __str__(self):
        return "{} -- {} to {}".format(self.content, self.author, self.receiver,)


class Skill(models.Model):
    TYPE_1 = "Type_1"
    TYPE_2 = "Type_2"
    TYPE_3 = "Type_3"
    TYPE_4 = "Type_4"

    SKILL_TYPES = (
        (TYPE_1, "Type_1"),
        (TYPE_2, "Type_2"),
        (TYPE_3, "Type_3"),
        (TYPE_4, "Type_4"))

    name = models.CharField(max_length=32)
    value = models.CharField(max_length=32, default=0)
    s_type = models.CharField(max_length=32, choices=SKILL_TYPES, verbose_name="Skill Type", default="Type_1")
    storyobject = models.ForeignKey('StoryObject')
    description = models.TextField(blank=True)

    def __str__(self):
        return "{}: {}".format(self.name, self.value)


class GameStats(models.Model):
    # Generic field for entering game information
    storyobject = models.ForeignKey('StoryObject')
    content = MarkdownField(blank=True)


class Statistic(models.Model):
    TYPE_1 = "Type_1"
    TYPE_2 = "Type_2"
    TYPE_3 = "Type_3"
    TYPE_4 = "Type_4"

    STAT_TYPES = (
        (TYPE_1, "Type_1"),
        (TYPE_2, "Type_2"),
        (TYPE_3, "Type_3"),
        (TYPE_4, "Type_4"))

    name = models.CharField(max_length=32)
    value = models.CharField(max_length=32, default=0)
    stat_type = models.CharField(
        max_length=32, choices=STAT_TYPES, verbose_name="Statistic Type",
         default="Type_1")
    storyobject = models.ForeignKey('StoryObject')
    description = models.TextField(blank=True)

    def __str__(self):
        return "{}: {}".format(self.name, self.value)


class CombatInfo(models.Model):
    title = models.CharField(max_length=32)
    data = models.CharField(max_length=128, default=0)
    storyobject = models.ForeignKey('StoryObject')

    def __str__(self):
        return "{}: {}".format(self.title, self.data)


class StoryObject(models.Model):

    CHARACTER = "Character"
    CREATURE = "Creature"
    THING = "Thing"
    FACTION = "Faction"
    ORGANIZATION = "Organization"
    TERRITORY = "Territory"
    PLACE = "Place"
    EVENT = "Event"

    CHAR_CHOICES = (
        (FACTION, "Faction"),
        (CHARACTER, "Character"),
        (CREATURE, "Creature"),
        (ORGANIZATION, "Organization"),
        (TERRITORY, "Territory"),
        (THING, "Thing"),
        (EVENT, "Event"),
    )

    creator = models.ForeignKey(User, unique=False, blank=True)
    name = models.CharField(max_length=128, unique=False)
    story = models.ForeignKey('Story', default=1)
    c_type = models.CharField(choices=CHAR_CHOICES, 
        max_length=32, default="Character", verbose_name="Story Object Type",
        help_text="Select a story object category.")
    role = models.CharField(max_length=256)
    description = MarkdownField(blank=True)

    image = models.ImageField(
        upload_to='profile_images/%Y/%m/%d/%H_%M_%S', default='profile_images/shadow_figure.jpeg')
    thumbnail = ImageSpecField(source='image',
        processors=[ResizeToFill(50, 50)],
        format='JPEG',
        options={'quality': 60}
        )
    slug = models.SlugField(unique=True, max_length=255)

    published = models.BooleanField(default=True,
        help_text="Elements that are NOT published will only be viewable in your Workshop.")

    def save(self, slug=None, creator=None, *args, **kwargs):
        self.story.object_count = F('object_count') + 1
        self.story.save()
        self.slug = slugify("{}-{}".format(self.story.id, self.name))
        super(StoryObject, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Place(StoryObject):
    latitude = models.FloatField(default=50.0)
    longitude = models.FloatField(default=-1.0)
    zoom = models.IntegerField(default=6, help_text="Sets the default zoom for your place")
    main_map = models.ForeignKey("MainMap", blank=True, null=True, verbose_name='Map',
                                help_text="Leave this blank for the default map, or choose from the list.")


class Relationship(models.Model):

    from_storyobject = models.ForeignKey(StoryObject, related_name="from_storyobject",
        verbose_name="Source of Relationship")
    to_storyobject = models.ForeignKey(StoryObject, related_name="to_storyobject",
        verbose_name="Object of Relationship",
        help_text="Enter the character or story object subject of the relationship here.")

    relationship_class = models.CharField(max_length=32,
        default='Ally',
        verbose_name="Relationship Description",
        help_text="Enter the type of relationship here. E.g.: Ally, Friend, Lover, etc.")

    weight = models.CharField(default="5", max_length=64,
        verbose_name="Numerical Rating",
        help_text="If your story uses it, enter a numerical rating for the relationship here.")

    relationship_description = models.CharField(max_length=128, unique=False,
        verbose_name="Details",
        help_text="Enter any additional details here.")

    def __str__(self):
        return '{} > {} >> {} ({}) - weight: {})'.format(
            self.from_storyobject, self.relationship_class,
            self.to_storyobject, self.relationship_description, self.weight)

    def save(self, *args, **kwargs):
        mail_format(self.to_storyobject,
            self.to_storyobject.name,
            self.from_storyobject.creator, 'New Relationship', self,
            noun="relationship", verb="added")
        super(Relationship, self).save(*args, **kwargs)



class Scene(models.Model):

    PROCEDURAL = "Prodecural"
    ACTION = "Action"
    SUSPENSE = "Suspense"
    QUESTION = "Question"
    REVEAL = "Reveal"
    DRAMATIC = "Dramatic"

    SCENE_TYPE_CHOICES = (
        (DRAMATIC, "Dramatic"),
        (ACTION, "Action"),
        (SUSPENSE, "Suspense"),
        (QUESTION, "Question"),
        (REVEAL, "Reveal"),
        (PROCEDURAL, "Procedural"))

    UP = "Up"
    DOWN = "Down"
    NEUTRAL = "Neutral"

    RESOLUTION_CHOICES = (
        (UP, "Up"),
        (DOWN, "Down"),
        (NEUTRAL, "Neutral"))

    title = models.CharField(max_length=128)
    scene_type = models.CharField(max_length=32, choices=SCENE_TYPE_CHOICES, default="Dramatic")
    purpose = models.CharField(max_length=128, blank=True)
    description = MarkdownField(blank=True)
    resolution = models.CharField(
        max_length=8, choices=RESOLUTION_CHOICES, default="Neutral")
    creator = models.ForeignKey(User, blank=True, null=True)
    place = models.ForeignKey(Place, blank=True, null=True, related_name="loc2scene")
    publication_date = models.DateTimeField(auto_now=True)
    order = models.PositiveSmallIntegerField(default=1)
    storyobjects = models.ManyToManyField(StoryObject, blank=True)
    chapter = models.ForeignKey("Chapter")
    published = models.BooleanField(default=True,
        help_text="Elements that are NOT published will only be viewable in your Workshop.")

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.chapter.story.object_count = F('object_count') + 1
        self.chapter.story.save()
        self.slug = slugify("{}-{}".format(self.chapter.story.id, self.title))
        super(Scene, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=128)
    description = MarkdownField(blank=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    story = models.ForeignKey("Story")
    number = models.PositiveSmallIntegerField(default=1,
        verbose_name="Chapter Number")
    published = models.BooleanField(default=True,
        help_text="Elements that are NOT published will only be viewable in your Workshop.")

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.story.object_count = F('object_count') + 1
        self.story.save()
        self.slug = slugify("{}-{}".format(self.story.id, self.title))
        super(Chapter, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.number, self.title)


class StoryOptions(models.Model):

    story = models.ForeignKey("Story")

    LIGHT = "Light"
    DARK = "Dark"

    THEME_CHOICES = (
        (LIGHT, 'Light'),
        (DARK, 'Dark'))

    map_tile = models.CharField(
        max_length=128, default="http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        help_text='''This field is used for Leaflet maps in the engine.
        The default tile set is openstreetmap.
        You probably shouldn't touch this unless you have another tileset in mind.''')
    base_latitude = models.FloatField(blank=True, default=50.0000)
    base_longitude = models.FloatField(blank=True, default=-1.3000)
    zoom = models.IntegerField(default=6, help_text="Sets the default zoom for your map")
    skill_type_name_1 = models.CharField(
        max_length=24, default="General", blank=True,
        help_text='''This field and the skill fields below set the name for different skill types in a game.
        They are optional, but if you are using skills of some kind, the first value should be set.''')
    skill_type_name_2 = models.CharField(
        max_length=24, default="Investigative", blank=True)
    skill_type_name_3 = models.CharField(
        max_length=24, default="Combat", blank=True)
    skill_type_name_4 = models.CharField(
        max_length=24, default="Knowledge", blank=True)

    statistic_type_name_1 = models.CharField(
        max_length=24, default="Physical", blank=True,
        help_text='''This field and the statistic fields below set the name for different stat types in a game.
        They are optional, but if you are using statistics of some kind, the first value should be set.''')
    statistic_type_name_2 = models.CharField(
        max_length=24, default="Mental", blank=True)
    statistic_type_name_3 = models.CharField(
        max_length=24, default="Social", blank=True)
    statistic_type_name_4 = models.CharField(
        max_length=24, default="Magic", blank=True)

    gamestats_toggle = models.BooleanField(default=True,
     help_text='''Check to enable a markdown field for entering game statistics.
        This is the default option, but you can choose specific tabbed fields below if you prefer.''',
        verbose_name="Enable Game Stats field?")
    stats_toggle = models.BooleanField(default=False,
     help_text="Check to enable statistics for this story object.",
        verbose_name="Enable Statistics?")
    skill_toggle = models.BooleanField(default=False,
     help_text="Check to enable skills for this story object.",
        verbose_name="Enable Skills?")
    combat_toggle = models.BooleanField(default=False,
     help_text="Check to enable combat info for this story object.",
        verbose_name="Enable Combat Info?")
    equipment_toggle = models.BooleanField(default=False,
     help_text="Check to enable equipment for this story object.",
        verbose_name="Enable Equipment?")
    gallery_toggle = models.BooleanField(default=False,
     help_text="Check to enable gallery images for this story object.",
        verbose_name="Enable Gallery Images?")
    social_toggle = models.BooleanField(default=False,
     help_text="Check to enable social functionality for this story object.",
        verbose_name="Enable Social Functions?")


class Story(models.Model):
    SUPERS = 'Supers'
    FANTASY = 'Fantasy'
    HORROR = 'Horror'
    HISTORICAL = 'Historical'
    SCI_FI = 'Science-Fiction'
    WESTERN = 'Western'
    DRAMA = 'Drama'
    COMEDY = 'Comedy'
    CRIME = 'Crime'
    FABLE = 'Fable'
    MYSTERY = 'Mystery'

    GENRE_CHOICES = (
        (SUPERS, 'Supers'),
        (FANTASY, 'Fantasy'),
        (HORROR, 'Horror'),
        (HISTORICAL, 'Historical'),
        (SCI_FI, "Science Fiction"),
        (WESTERN, 'Western'),
        (DRAMA, 'Drama'),
        (COMEDY, 'Comedy'),
        (CRIME, 'Crime'),
        (FABLE, 'Fable'),
        (MYSTERY, 'Mystery'),
    )

    LIGHT = "Light"
    DARK = "Dark"

    THEME_CHOICES = (
        (LIGHT, 'Light'),
        (DARK, 'Dark'))

    title = models.CharField(max_length=128)
    author = models.ForeignKey(User)
    publication_date = models.DateField(auto_now=True)
    setting = models.CharField(max_length=256)
    themes = models.CharField(max_length=256,
        help_text="Enter the themes for your story here.")
    description = MarkdownField(blank=True)
    genre = models.CharField(
        max_length=128, choices=GENRE_CHOICES, default='Fantasy')
    image = models.ImageField(
        upload_to='story_images/%Y/%m/%d/%H_%M_%S',
        default='profile_images/shadow_figure.jpeg')
    colour_theme = models.CharField(
        max_length=12, choices=THEME_CHOICES, default='Dark',
        help_text="Please note that the LIGHT field is not yet optimized.")
    published = models.BooleanField(default=True,
        help_text="Elements that are NOT published will only be viewable in your Workshop.")
    object_count = models.PositiveSmallIntegerField(default=0)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Story, self).save(*args, **kwargs)
        self.storyoptions = StoryOptions.objects.get_or_create(
            story=self)
        self.mainmap = MainMap.objects.get_or_create(
            name="{} Map".format(self.title),
            story=self)

    def __str__(self):
        return self.title


class MainMap(models.Model):
    name = models.CharField(max_length=64)
    story = models.ForeignKey(Story)
    base_latitude = models.FloatField(blank=True, default=50.000)
    base_longitude = models.FloatField(blank=True, default=-0.15)
    zoom = models.IntegerField(default=6, help_text="Sets the default zoom for your map")
    tiles = models.CharField(max_length=256, blank=True,
        default="http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png")
    published = models.BooleanField(default=True,
        help_text="Elements that are NOT published will only be viewable in your Workshop.")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify("{}-{}".format(self.story.id, self.name))
        super(MainMap, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    image = models.ImageField(
        upload_to='user_images/%Y/%m/%d',
        default='profile_images/shadow_figure.jpeg')
    own_notifications = models.BooleanField(default=False,
                                            help_text="Enable this to get email notifications for your own changes.")
    other_notifications = models.BooleanField(default=True,
                                              help_text="Enable this to get email notifications for changes other people make.")

    def __str__(self):
        return self.user.username


class Poster(models.Model):
    author = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=128)
    content = MarkdownField(blank=True)
    publication_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.content

