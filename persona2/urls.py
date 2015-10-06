from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from personas.models import StoryObject, Story, Location, Skill, Nation, Chapter, Scene, Ability, Statistic, Relationship, Place
from rest_framework import serializers, viewsets, routers, generics, pagination
from rest_framework.response import Response

# Serializers define the API representation


# StoryObject API
class StoryObjectSerializer(serializers.HyperlinkedModelSerializer):

    skills = serializers.StringRelatedField(
        many=True,
        read_only=True,
        source='skill_set')

    aspects = serializers.StringRelatedField(
        many=True,
        read_only=True,
        source='aspect_set')

    gamestats = serializers.StringRelatedField(
        read_only=True,
        source='gamestats_set')

    statistics = serializers.StringRelatedField(
        many=True,
        read_only=True,
        source='statistic_set')

    abilities = serializers.StringRelatedField(
        many=True,
        read_only=True,
        source='ability_set')

    combatinfo = serializers.StringRelatedField(
        many=True,
        read_only=True,
        source='combatinfo_set')

    equipment = serializers.StringRelatedField(
        read_only=True,
        source='equipment_set')

    to_relationships = serializers.StringRelatedField(
        many=True,
        read_only=True,
        source='to_storyobject')

    from_relationships = serializers.StringRelatedField(
        many=True,
        read_only=True,
        source='from_storyobject')

    class Meta:
        model = StoryObject
        fields = ("name", "story", "c_type", "role", "image", "nationality",
            "base_of_operations", "description", "gamestats", "equipment",
            "aspects", "abilities", "statistics", "skills", "combatinfo",
            "to_relationships", "from_relationships", "url")


class StoryObjectViewSet(viewsets.ModelViewSet):
    queryset = StoryObject.objects.all()
    serializer_class = StoryObjectSerializer


# Place API
class PlaceSerializer(serializers.HyperlinkedModelSerializer):

    aspects = serializers.StringRelatedField(
        many=True,
        read_only=True,
        source='aspect_set')

    gamestats = serializers.StringRelatedField(
        read_only=True,
        source='gamestats_set')

    to_relationships = serializers.StringRelatedField(
        many=True,
        read_only=True,
        source='to_storyobject')

    from_relationships = serializers.StringRelatedField(
        many=True,
        read_only=True,
        source='from_storyobject')

    class Meta:
        model = Place
        fields = ("name", "story", "c_type", "role", "image", "nationality",
            "base_of_operations", "description", "gamestats",
            "aspects", "latitude", "longitude",
            "to_relationships", "from_relationships", "url")


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


# Relationship API
class RelationshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relationship
        fields = ("to_storyobject", "from_storyobject", "relationship_class",
            "relationship_description", "weight")


class RelationshipViewSet(viewsets.ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer


# Nation API
class NationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Nation
        fields = ("name", "image", "description", "might", "intrigue",
            'magic', "wealth", "influence", "defense", "story", "url")


class NationViewSet(viewsets.ModelViewSet):
    queryset = Nation.objects.all()
    serializer_class = NationSerializer


# Location API
class LocationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Location
        fields = ("name", "image", "terrain", "features", "description",
            "nation", "latitude", "longitude", "story", "url")


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


# Scene API
class SceneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Scene
        fields = ("title", "scene_type", "purpose", "description",
            "resolution", "place", "chapter", "order", "url", "storyobjects")


class SceneViewSet(viewsets.ModelViewSet):
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer


# Chapter API
class ChapterSerializer(serializers.HyperlinkedModelSerializer):

    scenes = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="scene-detail",
        read_only=True,
        source="scene_set")

    class Meta:
        model = Chapter
        fields = ("title", "description", "story", "number", "url", "scenes")


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

# Story API
class StorySerializer(serializers.HyperlinkedModelSerializer):

    chapters = serializers.HyperlinkedRelatedField(
        queryset = Chapter.objects.all(),
        many=True,
        view_name="chapter-detail",
        source="chapter_set")

    storyobjects = serializers.HyperlinkedRelatedField(
        queryset = StoryObject.objects.all(),
        many=True,
        view_name="storyobject-detail",
        source="storyobject_set")

    nations = serializers.HyperlinkedRelatedField(
        queryset = Nation.objects.all(),
        many=True,
        view_name="nation-detail",
        source="nation_set")

    class Meta:
        model = Story
        fields = ("title", "setting", "themes", "description", "genre", "url",
            "chapters", "storyobjects", "nations")


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


router = routers.DefaultRouter()
router.register(r'story', StoryViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'storyobjects', StoryObjectViewSet)
router.register(r'scenes', SceneViewSet)
router.register(r'nations', NationViewSet)
router.register(r'locations', LocationViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'persona2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^personas/', include('personas.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r"^search/", include("watson.urls", namespace="watson")),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    #url(r'^about/', include('personas.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
            'serve',
            {'document_root': settings.MEDIA_ROOT}),)
