from django.contrib import admin
from personas.models import StoryObject, Relationship, Story, MainMap, Chapter, Scene, Ability, Aspect, Skill, Note, Communique, UserProfile, Statistic, CombatInfo, GalleryImage, ScratchPad, Equipment, Poster, GameStats, Place, StoryOptions
from personas.forms import RelationshipForm
from imagekit.admin import AdminThumbnail
#from leaflet.admin import LeafletGeoAdmin

class FlatPageAdmin(admin.ModelAdmin):
    fields = ('last_name', 'first_name')

class StoryObjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'creator', 'story', 'c_type', 'role')
    #admin_thumbnail = AdminThumbnail(image_field='thumbnail')

class StoryOptionsAdmin(admin.ModelAdmin):
    list_display = ('story',)

class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'creator', 'story', 'role')

class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'story', 'number')

class SceneAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'chapter', 'order',
        'scene_type', 'purpose', 'resolution')

class AspectAdmin(admin.ModelAdmin):
    list_display = ('name', 'details')

class PosterAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('storyobject', 's_type', 'name', 'value')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('creator', 'date', 'storyobject', 'place',
        'scene', 'chapter', 'story', 'rating')

class CommuniqueAdmin(admin.ModelAdmin):
    list_display = ('author', 'receiver', 'content', 'date', 'rating')

class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'storyobject')

class GameStatsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'storyobject', 'content')

class RelationshipAdmin(admin.ModelAdmin):
    form = RelationshipForm

class ScratchPadAdmin(admin.ModelAdmin):
    list_display = ('storyobject', 'content', 'pk')


# Register your models here.
admin.site.register(StoryObject, StoryObjectAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Relationship)
admin.site.register(Story, StoryAdmin)
admin.site.register(StoryOptions, StoryOptionsAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Scene, SceneAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(Aspect, AspectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Statistic)
admin.site.register(GameStats, GameStatsAdmin)
admin.site.register(CombatInfo)
admin.site.register(Equipment)
admin.site.register(Communique, CommuniqueAdmin)
admin.site.register(GalleryImage)
admin.site.register(ScratchPad, ScratchPadAdmin)
admin.site.register(UserProfile)
admin.site.register(Poster, PosterAdmin)
admin.site.register(MainMap)
#admin.site.register(LeafletGeoAdmin)

