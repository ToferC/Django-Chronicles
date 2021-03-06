from django import forms
from django.forms import widgets
from django.db.models import Q
from django.forms.models import modelform_factory, formset_factory
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from personas.models import StoryObject, Relationship, Aspect, Ability, Story, Scene, Chapter, Skill, Note, Communique, UserProfile, GalleryImage, MainMap
from personas.models import Statistic, CombatInfo, ScratchPad, Equipment, GameStats, Place, StoryOptions
from personas.personas_email import mail_format as mail_format
from django_markdown.widgets import MarkdownWidget
from django_markdown.fields import MarkdownFormField
from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineField

import datetime

# Choice fields for storyobjects

CHARACTER = "Character"
CREATURE = "Creature"
THING = "Thing"
FACTION = "Faction"
ORGANIZATION = "Organization"
TERRITORY = "Territory"
PLACE = "Place"
EVENT = "Event"


class StoryObjectForm(forms.ModelForm):
    class Meta:
        model = StoryObject
        fields = "__all__"
        exclude = ['slug', 'creator', 'story']
        widgets = {
        'c_type': forms.RadioSelect()
        }

    def __init__(self, *args, **kwargs):

        super(StoryObjectForm, self).__init__(*args, **kwargs)

        self.fields['c_type'].choices = (
        (FACTION, "Faction"),
        (CHARACTER, "Character"),
        (CREATURE, "Creature"),
        (ORGANIZATION, "Organization"),
        (TERRITORY, "Territory"),
        (THING, "Thing"),
        (EVENT, "Event"),
    )

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/personas/story/{{ story.slug }}/#storyobjects">Cancel</a>"""),
                Submit('save', 'Submit'),))

    def save(self, creator, story=None, commit=True):
        instance = super(StoryObjectForm, self).save(commit=False)
        instance.slug = slugify("{}-{}".format(story.title, instance.name))
        instance.creator = creator
        instance.story = story
        instance.save()
        return instance


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"
        exclude = ['slug', 'creator', 'story', 'c_type']

    def __init__(self, *args, **kwargs):

        try:
            self.story = kwargs.pop('story')
        except KeyError:
            self.story = None

        super(PlaceForm, self).__init__(*args, **kwargs)

        if self.story:
            self.fields['main_map'].queryset = MainMap.objects.filter(
                story=self.story).filter(published=True).order_by('name')

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/personas/story/{{ story.slug }}/#geography">Cancel</a>"""),
                Submit('save', 'Submit'),))

    def save(self, creator, story=None, commit=True):
        instance = super(PlaceForm, self).save(commit=False)
        instance.slug = slugify("{}-{}".format(story.title, instance.name))
        instance.creator = creator
        instance.c_type = "Place"
        instance.story = story
        instance.save()
        return instance

###
###

class BatchStoryObjectForm(forms.ModelForm):

    class Meta:
        model = StoryObject
        fields = ["name", "role", "c_type", "description", "image"]

class BatchFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(BatchFormSetHelper, self).__init__(*args, **kwargs)

        self.form_method = 'post'
        self.form_tag = False
        self.layout = Layout('name','role','c_type', 'description', 'image'
            )
        self.render_required_fields = True
        self.add_input(Submit("submit", "Save"))


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ["name", "value", "s_type"]

    def __init__(self, *args, **kwargs):
        try:
            self.storyobject = kwargs.pop('storyobject')
        except KeyError:
            self.storyobject = None

        choice_story = Story.objects.get(storyobject=self.storyobject)
        storyoptions = StoryOptions.objects.get(story=choice_story)

        context_choices = [('Type_1', getattr(storyoptions, 'skill_type_name_1')),
            ('Type_2', getattr(storyoptions, 'skill_type_name_2')),
            ('Type_3', getattr(storyoptions, 'skill_type_name_3')),
            ('Type_4', getattr(storyoptions, 'skill_type_name_4'))]

        INITIAL_CHOICES = [1, 2, 3 ,4]

        s_type = forms.ChoiceField()

        super(SkillForm, self).__init__(*args, **kwargs)

        self.fields['s_type'].choices = context_choices

        self.helper = FormHelper(self)
        self.layout = Layout(InlineField('name','value'),
            's_type',
        )
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#skills">Cancel</a>"""),
                Submit('save', 'Submit'),))


class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ["name", "value", "stat_type"]

    def __init__(self, *args, **kwargs):

        try:
            self.storyobject = kwargs.pop('storyobject')
        except KeyError:
            self.storyobject = None

        choice_story = Story.objects.get(storyobject=self.storyobject)
        storyoptions = StoryOptions.objects.get(story=choice_story)

        context_choices = [('Type_1', getattr(storyoptions, 'statistic_type_name_1')),
            ('Type_2', getattr(storyoptions, 'statistic_type_name_2')),
            ('Type_3', getattr(storyoptions, 'statistic_type_name_3')),
            ('Type_4', getattr(storyoptions, 'statistic_type_name_4'))]

        INITIAL_CHOICES = [1, 2, 3 ,4]

        stat_type = forms.ChoiceField()

        super(StatisticForm, self).__init__(*args, **kwargs)

        self.fields['stat_type'].choices = context_choices

        self.helper = FormHelper(self)
        self.layout = Layout(InlineField('name','value'),
            'stat_type',
        )
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#abilities">Cancel</a>"""),
                Submit('save', 'Submit'),))


class CombatInfoForm(forms.ModelForm):
    class Meta:
        model = CombatInfo
        fields = ["title", "data"]

    def __init__(self, *args, **kwargs):
        super(CombatInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.layout = Layout(InlineField('title','data'))
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#combat">Cancel</a>"""),
                Submit('save', 'Submit'),))


class ScratchPadForm(forms.ModelForm):
    class Meta:
        model = ScratchPad
        fields = ['content',]

    def __init__(self, *args, **kwargs):
        super(ScratchPadForm, self).__init__(*args, **kwargs)

        #self.fields['content'] = forms.CharField(widget=MarkdownWidget())

        self.helper = FormHelper(self)
        self.layout = Layout(InlineField('content',))
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#combat">Cancel</a>"""),
                Submit('snapshot', 'Submit'),))


class GameStatsForm(forms.ModelForm):
    class Meta:
        model = GameStats
        fields = ['content',]

    def __init__(self, *args, **kwargs):
        super(GameStatsForm, self).__init__(*args, **kwargs)

        #self.fields['content'] = forms.CharField(widget=MarkdownWidget())

        self.helper = FormHelper(self)
        self.layout = Layout(InlineField('content',))
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#gamestats">Cancel</a>"""),
                Submit('snapshot', 'Submit'),))


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['content',]

    def __init__(self, *args, **kwargs):
        super(EquipmentForm, self).__init__(*args, **kwargs)

        #self.fields['content'] = forms.CharField(widget=MarkdownWidget())

        self.helper = FormHelper(self)
        self.layout = Layout(InlineField('content',))
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#combat">Cancel</a>"""),
                Submit('record', 'Submit'),))


class SkillFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SkillFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.layout = Layout(InlineField('name','value'),
            's_type',
        )
        self.render_required_fields = True,


class AspectForm(forms.ModelForm):
    class Meta:
        model = Aspect
        fields = ['name', 'label', 'details']

    def __init__(self, *args, **kwargs):
        super(AspectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#details">Cancel</a>"""),
                Submit('save', 'Submit'),))


class AspectFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AspectFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.layout = Layout(
            'label',
            'name',
        )
        self.render_required_fields = True,


class AbilityForm(forms.ModelForm):
    class Meta:
        model = Ability
        fields = ["name", "description",]

    def __init__(self, *args, **kwargs):
        super(AbilityForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.layout = Layout(
            'name',
            'description',
        )
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#abilities">
                        Cancel</a>"""),
                Submit('save', 'Submit'),)
            )


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ["image", "title"]

    def __init__(self, *args, **kwargs):
        super(GalleryImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.layout = Layout(InlineField('title','data'))
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#combat">Cancel</a>"""),
                Submit('save', 'Submit'),))


class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Relationship
        fields = ["to_storyobject", "relationship_class",
        "relationship_description", "weight"]

    def __init__(self, *args, **kwargs):
        try:
            self.story = kwargs.pop('story')
        except KeyError:
            self.story = None

        super(RelationshipForm, self).__init__(*args, **kwargs)

        if self.story:
            self.fields['to_storyobject'].queryset = StoryObject.objects.filter(
                story=self.story).filter(published=True).order_by('name')

        self.helper = FormHelper(self)
        self.layout = Layout(
            'name',
            'description',
        )
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#details">Cancel</a>"""),
                Submit('save', 'Submit'),))

def create_relationship_form(story, user):
    '''Returns a new model form which uses the correct queryset for story'''

    class BatchRelationshipForm(forms.ModelForm):

        class Meta:
            model = Relationship
            fields = ["from_storyobject", "to_storyobject", "relationship_class",
            "relationship_description", "weight"]

        def __init__(self, *args, **kwargs):
            super(BatchRelationshipForm, self).__init__(*args, **kwargs)
            self.fields['to_storyobject'].queryset = StoryObject.objects.filter(
                story=story).filter(published=True).order_by('name')
            self.fields['from_storyobject'].queryset = StoryObject.objects.filter(
                story=story).filter(published=True).filter(
                Q(creator=user) | Q(story__author=user)).order_by('name')

    return BatchRelationshipForm


class RelationshipFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(RelationshipFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.layout = Layout(
            "from_storyobject", "to_storyobject", "relationship_class",
            "relationship_description", "weight",
        )
        self.render_required_fields = True,
        self.add_input(Submit("submit", "Save"))


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = "__all__"
        exclude = ['slug', 'author', 'publication_date',
        'object_count']

    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/">Cancel</a>"""),
                Submit('save', 'Submit'),))

    def save(self, author, commit=True):
        instance = super(StoryForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.author = author
        instance.publication_date = datetime.datetime.now()
        instance.save()
        return instance


class StoryOptionsForm(forms.ModelForm):
    class Meta:
        model = StoryOptions
        fields = "__all__"
        exclude = ['story',]

    def __init__(self, *args, **kwargs):
        super(StoryOptionsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/">Cancel</a>"""),
                Submit('save', 'Submit'),))


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ["title", "number", "description", "published"]

    def __init__(self, *args, **kwargs):

        try:
            self.story = kwargs.pop('story')
        except KeyError:
            self.story = None

        super(ChapterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.layout = Layout(
            'title',
            'description',
        )
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/story/{{ story.slug }}/#chapters">Cancel</a>"""),
                Submit('save', 'Submit'),))


class SceneForm(forms.ModelForm):
    storyobjects = forms.ModelMultipleChoiceField(
        queryset = StoryObject.objects.exclude(c_type="Place"))

    class Meta:
        model = Scene

        fields = "__all__"
        exclude = ["slug", "creator", "publication_date"]

    def __init__(self, *args, **kwargs):
        try:
            self.story = kwargs.pop('story')
        except KeyError:
            self.story = None

        super(SceneForm, self).__init__(*args, **kwargs)

        if self.story:
            self.fields['place'].queryset = Place.objects.filter(
                story=self.story).filter(published=True).order_by('name')
            self.fields['storyobjects'].queryset = StoryObject.objects.filter(
                story=self.story).filter(published=True).exclude(c_type="Place").order_by('name')
            self.fields['storyobjects'].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields['chapter'].queryset = Chapter.objects.filter(
                story=self.story).filter(published=True).order_by("number")

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/chapter/{{ chapter.slug }}">Cancel</a>"""),
                Submit('save', 'Submit'),))


class MainMapForm(forms.ModelForm):
    class Meta:
        model = MainMap
        fields = ["name", "base_latitude", "base_longitude", "zoom", "tiles"]

    def __init__(self, *args, **kwargs):
        try:
            self.story = kwargs.pop('story')
        except KeyError:
            self.story = None

        super(MainMapForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/story/{{ story.slug }}/#geography">Cancel</a>"""),
                Submit('save', 'Submit'),))


class NoteForm(forms.ModelForm):
    # Something isn't working here

    class Meta:
        model = Note
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/">Cancel</a>"""),
                Submit('save', 'Submit'),))

    def save(self, commit=False, *args, **kwargs):
        instance = super(NoteForm, self).save(commit=False)

        try:
            instance.creator = kwargs.pop('creator')
        except KeyError:
            instance.creator = None

        try:
            instance.storyobject = kwargs.pop('storyobject')
            mail_format(instance.storyobject, instance.storyobject.name,
                instance.creator, instance.title, instance.content)

        except KeyError:
            pass

        try:
            instance.scene = kwargs.pop('scene')
            mail_format(instance.scene, instance.scene.title,
                instance.creator, instance.title, instance.content)

        except KeyError:
            pass

        try:
            instance.place = kwargs.pop('place')
            mail_format(instance.place, instance.place.name,
                instance.creator, instance.title, instance.content)

        except KeyError:
            pass
        try:
            instance.chapter = kwargs.pop('chapter')
            mail_format(instance.chapter, instance.chapter.title,
                instance.creator, instance.title, instance.content)

        except KeyError:
            pass

        try:
            instance.story = kwargs.pop('story')
            mail_format(instance.story, instance.story.title,
                instance.creator, instance.title, instance.content)
        except KeyError:
            pass

        instance.save()
        return instance


class CommuniqueForm(forms.ModelForm):
    # Something isn't working here

    class Meta:
        model = Communique
        fields = ('content', 'receiver')

    def __init__(self, *args, **kwargs):

        try:
            self.story = kwargs.pop('story')
        except KeyError:
            self.story = None

        super(CommuniqueForm, self).__init__(*args, **kwargs)

        if self.story:
            self.fields['receiver'].queryset = StoryObject.objects.filter(
                story=self.story).order_by('name')


        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#social">Cancel</a>"""),
                Submit('send', 'Submit'),))

    def save(self, author, commit):
        instance = super(CommuniqueForm, self).save(commit=False)
        instance.author = author
        instance.save(author)
        mail_format(instance.receiver, instance.receiver.name,
            instance.author, 'New Communique', instance.content,
            noun="communique", verb="sent")
        return instance


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    captcha = CaptchaField()
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'captcha')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/">Cancel</a>"""),
                Submit('save', 'Submit'),))



class UserProfileForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = UserProfile
        fields = ('website', 'image')


class SignupForm(forms.Form):
    # additional fields for the Google social auth
    own_notifications = forms.BooleanField(help_text="Enable this to get email notifications for your own changes.")
    other_notifications = forms.BooleanField(help_text="Enable this to get email notifications for changes other people make.")

    def signup(self, request, user):
        # saving the new fields to the UserProfile
        userprofile = UserProfile(user=user)
        userprofile.own_notifications = self.cleaned_data['own_notifications']
        userprofile.other_notifications = self.cleaned_data['other_notifications']
        user.save()
        userprofile.save()