from django.conf.urls import patterns, url
from personas import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    
    url(r'^add_character/(?P<story_title_slug>[\w\-]+)/$', views.add_character, name='add_character'),
    url(r'^delete_character/(?P<pk>\d+)/$', views.delete_character, name='delete_character'),
    url(r'^edit_character/(?P<pk>\d+)/$', views.edit_character, name='edit_character'),

    url(r'^add_trait/(?P<character_name_slug>[\w\-]+)/$', views.add_trait, name='add_trait'),
    url(r'^delete_trait/(?P<pk>\d+)/$', views.delete_trait, name='delete_trait'),
    url(r'^edit_trait/(?P<pk>\d+)/$', views.edit_trait, name='edit_trait'),

    url(r'^add_skills/(?P<character_name_slug>[\w\-]+)/$', views.add_skills, name='add_skills'),
    url(r'^delete_skill/(?P<pk>\d+)/$', views.delete_skill, name='delete_skill'),
    url(r'^edit_skill/(?P<pk>\d+)/$', views.edit_skill, name='edit_skill'),

    url(r'^add_statistics/(?P<character_name_slug>[\w\-]+)/$', views.add_statistics, name='add_statistics'),
    url(r'^delete_statistic/(?P<pk>\d+)/$', views.delete_statistic, name='delete_statistic'),
    url(r'^edit_statistic/(?P<pk>\d+)/$', views.edit_statistic, name='edit_statistic'),

    url(r'^add_combat_info/(?P<character_name_slug>[\w\-]+)/$', views.add_combat_info, name='add_combat_info'),
    url(r'^delete_combat_info/(?P<pk>\d+)/$', views.delete_combat_info, name='delete_combat_info'),
    url(r'^edit_combat_info/(?P<pk>\d+)/$', views.edit_combat_info, name='edit_combat_info'),

    url(r'^add_ability/(?P<character_name_slug>[\w\-]+)/$', views.add_ability, name='add_ability'),
    url(r'^delete_ability/(?P<pk>\d+)/$', views.delete_ability, name='delete_ability'),
    url(r'^edit_ability/(?P<pk>\d+)/$', views.edit_ability, name='edit_ability'),

    url(r'^add_relationships/(?P<character_name_slug>[\w\-]+)/$', views.add_relationships, name='add_relationships'),
    url(r'^delete_relationship/(?P<pk>\d+)/$', views.delete_relationship, name='delete_relationship'),
    url(r'^edit_relationship/(?P<pk>\d+)/$', views.edit_relationship, name='edit_relationship'),

    url(r'^add_membership/(?P<character_name_slug>[\w\-]+)/$', views.add_membership, name='add_membership'),

    url(r'^create_story/$', views.create_story, name="create_story"),
    url(r'^delete_story/(?P<pk>\d+)/$', views.delete_story, name='delete_story'),
    url(r'^edit_story/(?P<pk>\d+)/$', views.edit_story, name='edit_story'),

    url(r'^add_chapter/(?P<story_title_slug>[\w\-]+)/$', views.add_chapter, name='add_chapter'),
    url(r'^add_scene/(?P<story_title_slug>[\w\-]+)/$', views.add_scene, name='add_scene'),
    url(r'^add_location/(?P<story_title_slug>[\w\-]+)/$', views.add_location, name='add_location'),
    url(r'^add_organization/(?P<story_title_slug>[\w\-]+)/$', views.add_organization, name='add_organization'),
    url(r'^add_artifact/(?P<slug>[\w\-]+)/$', views.add_artifact, name='add_artifact'),
    url(r'^register/$', views.register, name='register'),
    url(r'^collections/$', views.collections, name='collections'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^mainmap/(?P<mainmap_slug>[\w\-]+)/$', views.mainmap, name='mainmap'),
    url(r'^character/(?P<character_name_slug>[\w\-]+)/$', views.character, name='character'),
    url(r'^artifact/(?P<artifact_name_slug>[\w\-]+)/$', views.artifact, name='artifact'),
    url(r'^location/(?P<location_name_slug>[\w\-]+)/$', views.location, name='location'),
    url(r'^organization/(?P<organization_name_slug>[\w\-]+)/$', views.organization, name='organization'),
    url(r'^nation/(?P<nation_name_slug>[\w\-]+)/$', views.nation, name='nation'),
    url(r'^scene/(?P<scene_name_slug>[\w\-]+)/$', views.scene, name='scene'),
    url(r'^chapter/(?P<chapter_name_slug>[\w\-]+)/$', views.chapter, name='chapter'),
    url(r'^story/(?P<story_name_slug>[\w\-]+)/$', views.story, name='story'),
#url(r'^data.geojson$', GeoJSONLayerView.as_view(model=MushroomSpot), name='data'),
    )