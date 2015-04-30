from django.contrib import admin
from personas.models import Character, Relationship, Organization, Membership, Location, Nation, Story, MainMap, Chapter, Scene, SpecialAbility, Trait, Item, Skill, Note, Communique, UserProfile, Statistic, CombatInfo, GalleryImage, ScratchPad
from personas.forms import RelationshipForm
#from leaflet.admin import LeafletGeoAdmin

class FlatPageAdmin(admin.ModelAdmin):
    fields = ('last_name', 'first_name', 'nationality', 'base_of_operations')

class CharacterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'story', 'nationality', 'base_of_operations')

class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'story', 'nation', 'terrain', 'features')

class NationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ChapterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class SceneAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')

class TraitAdmin(admin.ModelAdmin):
    pass

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('organization', 'character', 'rank', 'role')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('character', 's_type', 'name', 'value')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('creator', 'date', 'character', 'location', 'item', 
        'organization', 'scene', 'chapter', 'story', 'organization' ,'rating')

class CommuniqueAdmin(admin.ModelAdmin):
    list_display = ('author', 'receiver', 'content', 'date', 'rating')

class SpecialAbilityAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class RelationshipAdmin(admin.ModelAdmin):
    form = RelationshipForm

class ScratchPadAdmin(admin.ModelAdmin):
    list_display = ('character', 'content', 'pk')


# Register your models here.
admin.site.register(Character, CharacterAdmin)
admin.site.register(Relationship)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Nation, NationAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Scene, SceneAdmin)
admin.site.register(SpecialAbility, SpecialAbilityAdmin)
admin.site.register(Trait, TraitAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Statistic)
admin.site.register(CombatInfo)
admin.site.register(Communique, CommuniqueAdmin)
admin.site.register(GalleryImage)
admin.site.register(ScratchPad, ScratchPadAdmin)
admin.site.register(UserProfile)
admin.site.register(MainMap)
#admin.site.register(LeafletGeoAdmin)

