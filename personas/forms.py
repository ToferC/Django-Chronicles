from django import forms
from django.forms import widgets
from django.forms.models import modelform_factory
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from personas.models import Nation, Location, StoryObject, Organization, Relationship, Membership, Aspect, Ability, Item, Story, Scene, Chapter, Skill, Note, Communique, UserProfile, GalleryImage
from personas.models import Statistic, CombatInfo, ScratchPad
from django_markdown.widgets import MarkdownWidget
from django_markdown.fields import MarkdownFormField
from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineField

import datetime


class StoryObjectForm(forms.ModelForm):
    class Meta:
        model = StoryObject
        fields = "__all__"
        exclude = ['slug', 'creator', 'story']

    def __init__(self, *args, **kwargs):
        try:
            self.story = kwargs.pop('story')
        except KeyError:
            self.story = None

        super(StoryObjectForm, self).__init__(*args, **kwargs)
        if self.story:
            self.fields['base_of_operations'].queryset = Location.objects.filter(story=self.story)
            self.fields['nationality'].queryset = Nation.objects.filter(story=self.story)


        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/story/{{ story.slug }}/#storyobjects">Cancel</a>"""),
                Submit('save', 'Submit'),))

    def save(self, creator, story=None, commit=True):
        instance = super(StoryObjectForm, self).save(commit=False)
        instance.slug = slugify("{}-{}".format(story.title, instance.name))
        instance.creator = creator
        instance.story = story
        instance.save()
        return instance


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

        context_choices = [('Type_1', getattr(choice_story, 'skill_type_name_1')),
            ('Type_2', getattr(choice_story, 'skill_type_name_2')),
            ('Type_3', getattr(choice_story, 'skill_type_name_3')),
            ('Type_4', getattr(choice_story, 'skill_type_name_4'))]

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

        context_choices = [('Type_1', getattr(choice_story, 'statistic_type_name_1')),
            ('Type_2', getattr(choice_story, 'statistic_type_name_2')),
            ('Type_3', getattr(choice_story, 'statistic_type_name_3')),
            ('Type_4', getattr(choice_story, 'statistic_type_name_4'))]

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
        fields = ['name', 'label']

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


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ["organization",
        "role", "rank"]

    def __init__(self, *args, **kwargs):
        try:
            self.story = kwargs.pop('story')
        except KeyError:
            self.story = None

        super(MembershipForm, self).__init__(*args, **kwargs)
        if self.story:
            self.fields['organization'].queryset = Organization.objects.filter(
                location__story=self.story).distinct()

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#details">Cancel</a>"""),
                Submit('save', 'Submit'),))


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "description",]

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.layout = Layout(
            'name',
            'description',
        )
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/storyobject/{{ storyobject.slug }}/#abilities">Cancel</a>"""),
                Submit('save', 'Submit'),))


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
                story=self.story).order_by('name')

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


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = "__all__"
        exclude = ['slug', 'creator', 'publication_date']

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


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ["title", "number", "description",]

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
    storyobjects = forms.ModelMultipleChoiceField(queryset = StoryObject.objects.all())

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
            self.fields['location'].queryset = Location.objects.filter(
                story=self.story)
            self.fields['storyobjects'].queryset = StoryObject.objects.filter(
                story=self.story)
            self.fields['storyobjects'].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields['chapter'].queryset = Chapter.objects.filter(
                story=self.story)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/chapter/{{ chapter.slug }}">Cancel</a>"""),
                Submit('save', 'Submit'),))


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "terrain", "features", "description",
        "nation", "latitude", "longitude", "image"]

    def __init__(self, *args, **kwargs):
        try:
            self.story = kwargs.pop('story')
        except KeyError:
            self.story = None

        super(LocationForm, self).__init__(*args, **kwargs)

        if self.story:
            self.fields['nation'].queryset = Nation.objects.filter(
                story=self.story)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/story/{{ story.slug }}/#geography">Cancel</a>"""),
                Submit('save', 'Submit'),))


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ["name", "description", "purpose",
        "region", "location", "image"]

    def __init__(self, *args, **kwargs):
        try:
            self.story = kwargs.pop('story')
        except KeyError:
            self.story = None

        super(OrganizationForm, self).__init__(*args, **kwargs)

        if self.story:
            self.fields['location'].queryset = Location.objects.filter(
                story=self.story)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/story/{{ story.slug }}/#political">Cancel</a>"""),
                Submit('save', 'Submit'),))


class NationForm(forms.ModelForm):
    class Meta:
        model = Nation
        fields = ["name", "description", "might",
        "intrigue", "magic", "wealth", "influence", "defense", "image"]

    def __init__(self, *args, **kwargs):
        try:
            self.story = kwargs.pop('story')
        except KeyError:
            self.story = None

        super(NationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/story/{{ story.slug }}/#political">Cancel</a>"""),
                Submit('save', 'Submit'),))


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "description",]

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default"
                        href="/personas/story/{{ story.slug }}">Cancel</a>"""),
                Submit('save', 'Submit'),))



class NoteForm(forms.ModelForm):
    # Something isn't working here

    class Meta:
        model = Note
        fields = ('content',)

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
            instance.storyobject = kwargs.pop('storyobject')
        except KeyError:
            pass
        try:
            instance.creator = kwargs.pop('creator')
        except KeyError:
            instance.creator = None
        try:
            instance.scene = kwargs.pop('scene')
        except KeyError:
            pass
        try:
            instance.location = kwargs.pop('location')
        except KeyError:
            pass
        try:
            instance.chapter = kwargs.pop('chapter')
        except KeyError:
            pass
        try:
            instance.story = kwargs.pop('story')
        except KeyError:
            pass
        try:
            instance.organization = kwargs.pop('organization')
        except KeyError:
            pass
        try:
            instance.nation = kwargs.pop('nation')
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

