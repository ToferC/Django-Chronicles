from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from personas import views
#from djgeojson.views import GeoJSONLayerView


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^workshop/(?P<user>[\w\-]+)/$', views.workshop, name="workshop"),
    url(r'^redirect_template', TemplateView.as_view(template_name="redirect_template.html")),

    url(r'^add_storyobject/(?P<story_title_slug>[\w\-]+)/(?P<c_type>[\w\-]+)/$', views.add_storyobject, name='add_storyobject'),
    url(r'^delete_storyobject/(?P<pk>\d+)/$', views.delete_storyobject, name='delete_storyobject'),
    url(r'^edit_storyobject/(?P<pk>\d+)/$', views.edit_storyobject, name='edit_storyobject'),

    url(r'^place/(?P<place_name_slug>[\w\-]+)/$', views.place, name='place'),
    url(r'^add_place/(?P<story_title_slug>[\w\-]+)/$', views.add_place, name='add_place'),
    url(r'^delete_place/(?P<pk>\d+)/$', views.delete_place, name='delete_place'),
    url(r'^edit_place/(?P<pk>\d+)/$', views.edit_place, name='edit_place'),

    url(r'^add_batch_storyobject/(?P<story_title_slug>[\w\-]+)/$', views.add_batch_storyobject, name='add_batch_storyobject'),
    url(r'^add_batch_relationship/(?P<story_title_slug>[\w\-]+)/$', views.add_batch_relationship, name='add_batch_relationship'),

    url(r'^add_gamestats/(?P<storyobject_name_slug>[\w\-]+)/$', views.add_gamestats, name='add_gamestats'),

    url(r'^delete_gamestats/(?P<pk>\d+)/$', views.delete_gamestats, name='delete_gamestats'),
    url(r'^edit_gamestats/(?P<pk>\d+)/$', views.edit_gamestats, name='edit_gamestats'),

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

    url(r'^create_story/$', views.create_story, name="create_story"),
    url(r'^delete_story/(?P<pk>\d+)/$', views.delete_story, name='delete_story'),
    url(r'^edit_story/(?P<pk>\d+)/$', views.edit_story, name='edit_story'),

    url(r'^edit_storyoptions/(?P<pk>\d+)/$', views.edit_storyoptions, name='edit_storyoptions'),


    url(r'^add_chapter/(?P<story_title_slug>[\w\-]+)/$', views.add_chapter, name='add_chapter'),
    url(r'^delete_chapter/(?P<pk>\d+)/$', views.delete_chapter, name='delete_chapter'),
    url(r'^edit_chapter/(?P<pk>\d+)/$', views.edit_chapter, name='edit_chapter'),

    url(r'^add_scene/(?P<story_title_slug>[\w\-]+)/$', views.add_scene, name='add_scene'),
    url(r'^delete_scene/(?P<pk>\d+)/$', views.delete_scene, name='delete_scene'),
    url(r'^edit_scene/(?P<pk>\d+)/$', views.edit_scene, name='edit_scene'),

    url(r'^add_mainmap/(?P<story_title_slug>[\w\-]+)/$', views.add_mainmap, name='add_mainmap'),
    url(r'^relationship_map/(?P<slug>[\w\-]+)/(?P<scope>[\w\-]+)/$', views.relationship_map, name='relationship_map'),

    url(r'^note/(?P<story_slug>[\w\-]+)/(?P<pk>\d+)/$', views.note, name='note'),
    url(r'^delete_note/(?P<pk>\d+)/$', views.delete_note, name='delete_note'),
    url(r'^edit_note/(?P<pk>\d+)/$', views.edit_note, name='edit_note'),

    url(r'^mainmap/(?P<main_map_slug>[\w\-]+)/$', views.main_map, name='mainmap'),
    url(r'^delete_mainmap/(?P<pk>\d+)/$', views.delete_mainmap, name='delete_mainmap'),
    url(r'^edit_mainmap/(?P<pk>\d+)/$', views.edit_mainmap, name='edit_mainmap'),

    url(r'^add_gallery_image/(?P<storyobject_slug>[\w\-]+)/$', views.add_gallery_image, name='add_gallery_image'),

    url(r'^register/$', views.register, name='register'),
    url(r'^collections/$', views.collections, name='collections'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^user_profile/$', views.user_profile, name='user_profile'),
    url(r'^storyobject/(?P<storyobject_name_slug>[\w\-]+)/$', views.storyobject, name='storyobject'),
    url(r'^scene/(?P<scene_name_slug>[\w\-]+)/$', views.scene, name='scene'),
    url(r'^chapter/(?P<chapter_name_slug>[\w\-]+)/$', views.chapter, name='chapter'),
    url(r'^story/(?P<story_name_slug>[\w\-]+)/$', views.story, name='story'),
#url(r'^data.geojson$', GeoJSONLayerView.as_view(model=MushroomSpot), name='data'),
    )