from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from personas import views
#from djgeojson.views import GeoJSONLayerView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^redirect_template', TemplateView.as_view(template_name="redirect_template.html")),
    
    url(r'^add_storyobject/(?P<story_title_slug>[\w\-]+)/$', views.add_storyobject, name='add_storyobject'),
    url(r'^delete_storyobject/(?P<pk>\d+)/$', views.delete_storyobject, name='delete_storyobject'),
    url(r'^edit_storyobject/(?P<pk>\d+)/$', views.edit_storyobject, name='edit_storyobject'),

    url(r'^add_aspect/(?P<storyobject_name_slug>[\w\-]+)/$', views.add_aspect, name='add_aspect'),
    url(r'^delete_aspect/(?P<pk>\d+)/$', views.delete_aspect, name='delete_aspect'),
    url(r'^edit_aspect/(?P<pk>\d+)/$', views.edit_aspect, name='edit_aspect'),

    url(r'^add_skills/(?P<storyobject_name_slug>[\w\-]+)/$', views.add_skills, name='add_skills'),
    url(r'^delete_skill/(?P<pk>\d+)/$', views.delete_skill, name='delete_skill'),
    url(r'^edit_skill/(?P<pk>\d+)/$', views.edit_skill, name='edit_skill'),

    url(r'^add_statistics/(?P<storyobject_name_slug>[\w\-]+)/$', views.add_statistics, name='add_statistics'),
    url(r'^delete_statistic/(?P<pk>\d+)/$', views.delete_statistic, name='delete_statistic'),
    url(r'^edit_statistic/(?P<pk>\d+)/$', views.edit_statistic, name='edit_statistic'),

    url(r'^add_combat_info/(?P<storyobject_name_slug>[\w\-]+)/$', views.add_combat_info, name='add_combat_info'),
    url(r'^delete_combat_info/(?P<pk>\d+)/$', views.delete_combat_info, name='delete_combat_info'),
    url(r'^edit_combat_info/(?P<pk>\d+)/$', views.edit_combat_info, name='edit_combat_info'),

    url(r'^add_ability/(?P<storyobject_name_slug>[\w\-]+)/$', views.add_ability, name='add_ability'),
    url(r'^delete_ability/(?P<pk>\d+)/$', views.delete_ability, name='delete_ability'),
    url(r'^edit_ability/(?P<pk>\d+)/$', views.edit_ability, name='edit_ability'),

    url(r'^add_relationships/(?P<storyobject_name_slug>[\w\-]+)/$', views.add_relationships, name='add_relationships'),
    url(r'^delete_relationship/(?P<pk>\d+)/$', views.delete_relationship, name='delete_relationship'),
    url(r'^edit_relationship/(?P<pk>\d+)/$', views.edit_relationship, name='edit_relationship'),

    url(r'^add_membership/(?P<storyobject_name_slug>[\w\-]+)/$', views.add_membership, name='add_membership'),
    url(r'^delete_membership/(?P<pk>\d+)/$', views.delete_membership, name='delete_membership'),
    url(r'^edit_membership/(?P<pk>\d+)/$', views.edit_membership, name='edit_membership'),

    url(r'^create_story/$', views.create_story, name="create_story"),
    url(r'^delete_story/(?P<pk>\d+)/$', views.delete_story, name='delete_story'),
    url(r'^edit_story/(?P<pk>\d+)/$', views.edit_story, name='edit_story'),

    url(r'^add_chapter/(?P<story_title_slug>[\w\-]+)/$', views.add_chapter, name='add_chapter'),
    url(r'^delete_chapter/(?P<pk>\d+)/$', views.delete_chapter, name='delete_chapter'),
    url(r'^edit_chapter/(?P<pk>\d+)/$', views.edit_chapter, name='edit_chapter'),

    url(r'^add_scene/(?P<story_title_slug>[\w\-]+)/$', views.add_scene, name='add_scene'),
    url(r'^delete_scene/(?P<pk>\d+)/$', views.delete_scene, name='delete_scene'),
    url(r'^edit_scene/(?P<pk>\d+)/$', views.edit_scene, name='edit_scene'),

    url(r'^add_location/(?P<story_title_slug>[\w\-]+)/$', views.add_location, name='add_location'),
    url(r'^delete_location/(?P<pk>\d+)/$', views.delete_location, name='delete_location'),
    url(r'^edit_location/(?P<pk>\d+)/$', views.edit_location, name='edit_location'),

    url(r'^add_organization/(?P<story_title_slug>[\w\-]+)/$', views.add_organization, name='add_organization'),
    url(r'^delete_organization/(?P<pk>\d+)/$', views.delete_organization, name='delete_organization'),
    url(r'^edit_organization/(?P<pk>\d+)/$', views.edit_organization, name='edit_organization'),

    url(r'^add_artifact/(?P<slug>[\w\-]+)/$', views.add_artifact, name='add_artifact'),
    url(r'^delete_artifact/(?P<pk>\d+)/$', views.delete_artifact, name='delete_artifact'),
    url(r'^edit_artifact/(?P<pk>\d+)/$', views.edit_artifact, name='edit_artifact'),

    url(r'^add_nation/(?P<story_title_slug>[\w\-]+)/$', views.add_nation, name='add_nation'),
    url(r'^delete_nation/(?P<pk>\d+)/$', views.delete_nation, name='delete_nation'),
    url(r'^edit_nation/(?P<pk>\d+)/$', views.edit_nation, name='edit_nation'),

    url(r'^note/(?P<story_slug>[\w\-]+)/(?P<pk>\d+)/$', views.note, name='note'),
    url(r'^delete_note/(?P<pk>\d+)/$', views.delete_note, name='delete_note'),
    url(r'^edit_note/(?P<pk>\d+)/$', views.edit_note, name='edit_note'),

    url(r'^add_gallery_image/(?P<storyobject_slug>[\w\-]+)/$', views.add_gallery_image, name='add_gallery_image'),

    url(r'^register/$', views.register, name='register'),
    url(r'^collections/$', views.collections, name='collections'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^mainmap/(?P<mainmap_slug>[\w\-]+)/$', views.mainmap, name='mainmap'),
    url(r'^storyobject/(?P<storyobject_name_slug>[\w\-]+)/$', views.storyobject, name='storyobject'),
    url(r'^artifact/(?P<artifact_name_slug>[\w\-]+)/$', views.artifact, name='artifact'),
    url(r'^location/(?P<location_name_slug>[\w\-]+)/$', views.location, name='location'),
    url(r'^organization/(?P<organization_name_slug>[\w\-]+)/$', views.organization, name='organization'),
    url(r'^nation/(?P<nation_name_slug>[\w\-]+)/$', views.nation, name='nation'),
    url(r'^scene/(?P<scene_name_slug>[\w\-]+)/$', views.scene, name='scene'),
    url(r'^chapter/(?P<chapter_name_slug>[\w\-]+)/$', views.chapter, name='chapter'),
    url(r'^story/(?P<story_name_slug>[\w\-]+)/$', views.story, name='story'),
#url(r'^data.geojson$', GeoJSONLayerView.as_view(model=MushroomSpot), name='data'),
    )