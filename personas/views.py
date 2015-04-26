from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy, reverse
from django.forms.formsets import formset_factory
from django.contrib.auth import logout, login, authenticate
from django.db.models import F, Q
from django.db.models.base import ObjectDoesNotExist
from django.views.generic.edit import DeleteView, UpdateView, FormView, CreateView
from crispy_forms.layout import Submit, HTML
from crispy_forms.helper import FormHelper
from personas.models import Nation, Location, Character, Organization, Relationship, Membership, Trait, SpecialAbility, Item, Story, MainMap, Chapter, Scene, Skill, Note, Communique
from personas.models import Statistic, CombatInfo, GalleryImage, ScratchPad
from personas.forms import CharacterForm, NoteForm, CommuniqueForm, UserForm, UserProfileForm, SkillForm, TraitForm, TraitFormSetHelper, SkillFormSetHelper, ItemForm, SpecialAbilityForm, RelationshipForm
from personas.forms import StoryForm, ChapterForm, SceneForm, LocationForm, ItemForm, OrganizationForm, MembershipForm, StatisticForm, CombatInfoForm, NationForm, ScratchPadForm

from datetime import datetime

# Normal Views

def index(request):
    context_dict = {}

    try:
        stories = Story.objects.all()

        context_dict['stories'] = stories

    except Story.DoesNotExist:
        pass

    return render(request, 'personas/index.html', context_dict)


def collections(request):
    character_list = Character.objects.all()
    location_list = Location.objects.all()
    organization_list = Organization.objects.all()

    context_dict = {'boldmessage': "Personas", 'characters': character_list,
        'locations': location_list, 'organizations': organization_list}

    return render(request, 'personas/collections.html', context_dict)


def about(request):
    return HttpResponse(
        "<h1>Welcome to the about page!</h1> <a href='/personas/'>Main</a>")


def location(request, location_name_slug):

    context_dict = {}

    try:
        location = Location.objects.get(slug=location_name_slug)
        story = location.story

        context_dict['story'] = Story.objects.get(location=location)

        context_dict['location'] = location
        context_dict['location_name'] = location.name
        context_dict['creator'] = location.creator
        context_dict['image'] = location.image
        context_dict['terrain'] = location.terrain
        context_dict['features'] = location.features
        context_dict['description'] = location.description
        context_dict['nation'] = location.nation
        context_dict['latitude'] = location.latitude
        context_dict['longitude'] = location.longitude
        context_dict['slug'] = location.slug
        context_dict['scenes'] = Scene.objects.filter(
            location__name=location.name)
        context_dict['organizations'] = Organization.objects.filter(
            location__name=location.name).distinct()
        context_dict['characters'] = Character.objects.filter(
            base_of_operations__name=location.name)

        context_dict['notes'] = Note.objects.filter(location__name=location.name)

        if request.method == 'POST':
            if form.is_valid():

                form = context_dict['form']
                post_scene = scene
                post_creator = request.user
                form.save(scene=post_scene, creator=post_creator, commit=True)

                return HttpResponseRedirect("")

        else:

            context_dict['form'] = NoteForm()

    except Location.DoesNotExist:
        pass

    return render(request, 'personas/location.html', context_dict)


def scene(request, scene_name_slug):

    context_dict = {}

    try:
        scene = Scene.objects.get(slug=scene_name_slug)

        context_dict['scene'] = scene
        context_dict['scene_title'] = scene.title
        context_dict['slug'] = scene_name_slug
        context_dict['location'] = scene.location
        context_dict['description'] = scene.description
        context_dict['time'] = scene.time
        context_dict['characters'] = Character.objects.filter(scene__title=scene.title)

        context_dict['story'] = Story.objects.get(chapter__scene__title=scene.title)
        context_dict['chapter'] = Chapter.objects.get(scene__title=scene.title)

        context_dict['notes'] = Note.objects.filter(
            scene__title=scene.title)[0:10]

        form = NoteForm(request.POST or None)
        context_dict['form'] = form

        if request.method == 'POST':
            if form.is_valid():

                form = context_dict['form']
                post_scene = scene
                post_creator = request.user
                form.save(scene=post_scene, creator=post_creator, commit=True)

                return HttpResponseRedirect("")

        else:

            context_dict['form'] = NoteForm()

    except Scene.DoesNotExist:
        pass

    return render(request, 'personas/scene.html', context_dict)


def artifact(request, artifact_name_slug):

    context_dict = {}

    try:
        artifact = Item.objects.get(slug=artifact_name_slug)
        story = artifact.story
        character = artifact.character

        context_dict['artifact'] = artifact
        context_dict['description'] = artifact.description
        context_dict['character'] = character
        context_dict['story'] = story
        context_dict['abilities'] = SpecialAbility.objects.filter(item__name=artifact.name)

        context_dict['notes'] = Note.objects.filter(
            item__name=artifact.name)[0:10]

        form = NoteForm(request.POST or None)
        context_dict['form'] = form

        if request.method == 'POST':
            if form.is_valid():

                form = context_dict['form']
                post_artifact = artifact
                post_creator = request.user
                form.save(artifact=post_artifact, creator=post_creator, commit=True)

                return HttpResponseRedirect("")

        else:

            context_dict['form'] = NoteForm()

    except Item.DoesNotExist:
        pass

    return render(request, 'personas/artifact.html', context_dict)


def organization(request, organization_name_slug):

    context_dict = {}

    try:
        organization = Organization.objects.get(slug=organization_name_slug)
        members = Membership.objects.filter(organization=organization)
        story = Story.objects.get(location__organization=organization)

        context_dict['organization'] = organization
        context_dict['members'] = members
        context_dict['story'] = story

        context_dict['notes'] = Note.objects.filter(
            organization__name=organization.name)[0:10]

        form = NoteForm(request.POST or None)
        context_dict['form'] = form

        if request.method == 'POST':
            if form.is_valid():

                form = context_dict['form']
                post_organization = organization
                post_creator = request.user
                form.save(organization=post_organization, creator=post_creator, commit=True)

                return HttpResponseRedirect("")

        else:

            context_dict['form'] = NoteForm()

    except Organization.DoesNotExist:
        pass

    return render(request, 'personas/organization.html', context_dict)


def nation(request, nation_name_slug):

    context_dict = {}

    try:
        nation = Nation.objects.get(slug=nation_name_slug)
        story = Story.objects.get(nation=nation)

        context_dict['nation'] = nation
        context_dict['story'] = story
        context_dict['locations'] = Location.objects.filter(
            nation=nation).distinct()

        context_dict['notes'] = Note.objects.filter(
            nation__name=nation.name)[0:10]

        form = NoteForm(request.POST or None)
        context_dict['form'] = form

        if request.method == 'POST':
            if form.is_valid():

                form = context_dict['form']
                post_nation = nation
                post_creator = request.user
                form.save(nation=post_nation, creator=post_creator, commit=True)

                return HttpResponseRedirect("")

        else:

            context_dict['form'] = NoteForm()

    except Nation.DoesNotExist:
        pass

    return render(request, 'personas/nation.html', context_dict)


def character(request, character_name_slug):

    context_dict = {}

    try:
        character = Character.objects.get(slug=character_name_slug)

        context_dict['character_name'] = character.name
        context_dict['character'] = character
        context_dict['creator'] = character.creator
        context_dict['story'] = character.story
        context_dict['c_type'] = character.c_type
        context_dict['xp'] = character.xp
        context_dict['description'] = character.description

        # Set up ScratchPad for character
        try:
            scratchpad = ScratchPad.objects.get(
                character__name=character.name)
        except ScratchPad.DoesNotExist:
            scratchpad = ScratchPad(character=character, creator=request.user,
                content="Enter info here and save to update", date=datetime.now())

        context_dict['aspects'] = Trait.objects.filter(
            character__name=character.name)

        context_dict['type_1_statistics'] = Statistic.objects.filter(
            character__name=character.name).filter(stat_type="Type_1")
        context_dict['type_2_statistics'] = Statistic.objects.filter(
            character__name=character.name).filter(stat_type="Type_2")
        context_dict['type_3_statistics'] = Statistic.objects.filter(
            character__name=character.name).filter(stat_type="Type_3")
        context_dict['type_4_statistics'] = Statistic.objects.filter(
            character__name=character.name).filter(stat_type="Type_4")

        context_dict['type_1_skills'] = Skill.objects.filter(
            character__name=character.name).filter(s_type="Type_1")
        context_dict['type_2_skills'] = Skill.objects.filter(
            character__name=character.name).filter(s_type="Type_2")
        context_dict['type_3_skills'] = Skill.objects.filter(
            character__name=character.name).filter(s_type="Type_3")
        context_dict['type_4_skills'] = Skill.objects.filter(
            character__name=character.name).filter(s_type="Type_4")

        context_dict['combat_info'] = CombatInfo.objects.filter(
            character__name=character.name)

        context_dict['artifacts'] = Item.objects.filter(
            character__name=character.name)
        context_dict['relationships'] = Relationship.objects.filter(
            Q(from_character__name=character.name) |
            Q(to_character__name=character.name))

        context_dict['abilities'] = SpecialAbility.objects.filter(
            character__name=character.name)
        context_dict['notes'] = Note.objects.filter(
            character__name=character.name)

        context_dict['gallery_images'] = GalleryImage.objects.filter(
            character=character)

        context_dict['communiques'] = Communique.objects.filter(
            Q(author__name=character.name) |
            Q(receiver__name=character.name))

        context_dict['nationality'] = character.nationality
        context_dict['birthplace'] = character.birthplace
        context_dict['base_of_operations'] = character.base_of_operations
        context_dict['c_type'] = character.c_type
        context_dict['memberships'] = Membership.objects.filter(character=character)

        context_dict['image'] = character.image

        # Note Form Section
        noteform = NoteForm(request.POST, prefix="note")
        communique_form = CommuniqueForm(request.POST, prefix="comm")

        if request.method == 'POST':

            if 'save' in request.POST:
                creator = request.user
                note_subject = character

                noteform = NoteForm(request.POST)

                if noteform.is_valid():
                    noteform.save(
                        creator=creator, character=note_subject, commit=True)

                    return HttpResponseRedirect("/personas/character/{}/#notes".format(character_name_slug))

                else:
                    print (context_dict['noteform'].errors)

            elif 'send' in request.POST:
                post_creator = character

                communique_form = CommuniqueForm(request.POST)

                if communique_form.is_valid():
                    communique_form.save(author=post_creator, commit=True)
                    
                    return HttpResponseRedirect("/personas/character/{}/#social".format(character_name_slug))

                else:
                    print (context_dict['communique_form'].errors)

            if 'snapshot' in request.POST:

                scratchpadform = ScratchPadForm(request.POST or None, instance=scratchpad)

                if scratchpadform.is_valid():
                    scratchpadform.character = character

                    scratchpad.save()

                    context_dict['scratchpadform'] = ScratchPadForm(instance=scratchpad)

                    return HttpResponseRedirect("/personas/character/{}/#combat".format(character_name_slug))

                else:
                    print (context_dict['scratchpadform'].errors)

        else:

            context_dict['noteform'] = NoteForm()
            context_dict['communique_form'] = CommuniqueForm(story=character.story)
            context_dict['scratchpadform'] = ScratchPadForm(instance=scratchpad)


    except Character.DoesNotExist:
        pass

    return render(request, 'personas/character.html', context_dict)


def chapter(request, chapter_name_slug):

    context_dict = {}

    try:
        chapter = Chapter.objects.get(slug=chapter_name_slug)
        scenes = Scene.objects.filter(chapter__title=chapter.title).order_by(
            'time')

        context_dict['chapter_title'] = chapter.title
        context_dict['chapter'] = chapter
        context_dict['slug'] = chapter_name_slug
        context_dict['story'] = chapter.story
        context_dict['description'] = chapter.description

        context_dict['scenes'] = scenes

        context_dict['characters'] = Character.objects.filter(
            scene__chapter__title=chapter.title).distinct()
        context_dict['locations'] = Location.objects.filter(
            scene__chapter__title=chapter.title).distinct()


        context_dict['notes'] = Note.objects.filter(
            chapter__title=chapter.title)[0:10]

        form = NoteForm(request.POST or None)
        context_dict['form'] = form

        if request.method == 'POST':
            if form.is_valid():

                form = context_dict['form']
                post_chapter = chapter
                post_creator = request.user
                form.save(chapter=post_chapter, creator=post_creator, commit=True)

                return HttpResponseRedirect("")

        else:

            context_dict['form'] = NoteForm()

    except Chapter.DoesNotExist:
        pass

    return render(request, 'personas/chapter.html', context_dict)


def story(request, story_name_slug):

    context_dict = {}

    try:
        story = Story.objects.get(slug=story_name_slug)
        chapters = Chapter.objects.filter(story__title=story.title).order_by("number")

        context_dict['chapters'] = chapters

        context_dict['story'] = story
        context_dict['author'] = story.author
        context_dict['publication_date'] = story.publication_date
        context_dict['image'] = story.image
        context_dict['genre'] = story.genre
        context_dict['artifacts'] = Item.objects.filter(story=story).distinct()

        mainmaps = MainMap.objects.filter(
            story__title=story.title)
        context_dict['mainmaps'] = mainmaps

        #context_dict['slug'] = story_name_slug
        context_dict['description'] = story.description

        context_dict['notes'] = Note.objects.filter(
            story__title=story.title)

        scenes = Scene.objects.filter(chapter__story__title=story.title).distinct()

        context_dict['scenes'] = scenes

        context_dict['characters'] = Character.objects.filter(
                story=story).distinct().order_by('name')
        context_dict['locations'] = Location.objects.filter(
                story__title=story.title).distinct().order_by('name')
        context_dict['organizations'] = Organization.objects.filter(
                location__story__title=story.title).distinct().order_by('name')
        context_dict['nations'] = Nation.objects.filter(
            story=story).distinct().order_by('name')

        form = NoteForm(request.POST or None)
        context_dict['form'] = form

        if request.method == 'POST':
            if form.is_valid():

                form = context_dict['form']
                post_story = story
                post_creator = request.user
                form.save(story=post_story, creator=post_creator, commit=True)

                return HttpResponseRedirect("")

        else:

            context_dict['form'] = NoteForm()

    except Story.DoesNotExist:
        pass

    return render(request, 'personas/story.html', context_dict)


def mainmap(request, mainmap_slug):
    context_dict = {}

    mainmap = MainMap.objects.get(slug=mainmap_slug)

    try:
        context_dict['map_name'] = mainmap.name
        context_dict['story'] = mainmap.story
        context_dict['base_latitude'] = mainmap.base_latitude
        context_dict['base_longitude'] = mainmap.base_longitude
        context_dict['tile'] = mainmap.tiles

        context_dict['locations'] = Location.objects.filter(
            story=mainmap.story).distinct()

    except MainMap.DoesNotExist:
        pass

    return render(request, 'personas/mainmap.html', context_dict)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = request.user

            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            profile.save()

            registered = True

            return index(request)

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'personas/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 
        'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('/personas/')
            else:
                return HttpResponse("Your Personas account is disabled.")

        else:
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'personas/login.html', {})


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/personas/')


# Add content Views

@login_required
def add_character(request, story_title_slug):

    story = Story.objects.get(slug=story_title_slug)

    if request.method == 'POST':
        character_form = CharacterForm(request.POST, request.FILES)

        creator = request.user

        if character_form.is_valid():
            slug = slugify(character_form.cleaned_data['name'])

            character_form.save(creator=creator, story=story, commit=True)

            return HttpResponseRedirect("/personas/add_trait/{}".format(slug))

        else:
            print (character_form.errors)

    else:

        character_form = CharacterForm(story=story)

    return render(request, 'personas/add_character.html',
        {'character_form': character_form, 'story':story})


@login_required
def create_story(request):

    if request.method == 'POST':
        story_form = StoryForm(request.POST, request.FILES)

        creator = request.user

        if story_form.is_valid():
            slug = slugify(story_form.cleaned_data['title'])

            story_form.save(author=creator, commit=True)

            return HttpResponseRedirect("/personas/story/{}".format(slug))

        else:
            print (story_form.errors)

    else:

        story_form = StoryForm()

    return render(request, 'personas/create_story.html',
        {'story_form': story_form})


@login_required
def add_trait(request, character_name_slug):

    traits = Trait.objects.filter(character__slug=character_name_slug)

    character = Character.objects.get(slug=character_name_slug)
    story = character.story

    if request.method == 'POST':

        form = TraitForm(request.POST)

        if form.is_valid():
            trait_character = character

            #for f in formset:
            cd = form.cleaned_data
            if not cd.get('name'):
                pass
            else:
                name = cd.get('name')
                label = cd.get('label')
                trait = Trait(
                    name=name, label=label,
                    character=trait_character)

                trait.save()
                form = TraitForm()

            return HttpResponseRedirect("")

        else:
            print (form.errors)

    else:

        form = TraitForm()

    return render(request, 'personas/add_trait.html', {'form': form,
        'slug': character_name_slug, 'character': character,
        'traits': traits, 'story':story})


@login_required
def add_skills(request, character_name_slug):

    #SkillFormSet = formset_factory(SkillForm, extra=10, max_num=10)
    #helper = SkillFormSetHelper()

    skills = Skill.objects.filter(character__slug=character_name_slug)

    character = Character.objects.get(slug=character_name_slug)

    story = character.story

    type_1_skills = Skill.objects.filter(
            character__slug=character_name_slug).filter(s_type="Type_1")
    type_2_skills = Skill.objects.filter(
            character__slug=character_name_slug).filter(s_type="Type_2")
    type_3_skills = Skill.objects.filter(
            character__slug=character_name_slug).filter(s_type="Type_3")
    type_4_skills = Skill.objects.filter(
            character__slug=character_name_slug).filter(s_type="Type_4")

    if request.method == 'POST':

        form = SkillForm(request.POST or None, character=character)

        if form.is_valid():
            skill_character = character

            #for f in formset:
            cd = form.cleaned_data
            if cd.get('name') == None:
                pass
            else:
                name = cd.get('name')
                value = cd.get('value')
                s_type = cd.get('s_type')
                skill = Skill(
                    name=name, value=value, character=skill_character, s_type=s_type)

                skill.save()
                form = SkillForm(character=character)

            HttpResponseRedirect("")

        else:
            print (form.errors)

    else:
        form = SkillForm(character=character)

        #helper = SkillFormSetHelper()
        #helper.add_input(Submit("submit", "Save"))
        #helper.add_input(Submit("cancel", "Cancel"))

    return render(request, 'personas/add_skills.html', {'form': form,
        'slug': character_name_slug, 'character': character,
        'type_1_skills': type_1_skills, 'type_2_skills': type_2_skills,
        'type_3_skills': type_3_skills, 'type_4_skills': type_4_skills,
        'story':story})


@login_required
def add_statistics(request, character_name_slug):

    #StatisticFormSet = formset_factory(StatisticForm, extra=10, max_num=10)
    #helper = StatisticFormSetHelper()

    statistics = Statistic.objects.filter(character__slug=character_name_slug)

    character = Character.objects.get(slug=character_name_slug)

    story = character.story

    type_1_statistics = Statistic.objects.filter(
            character__slug=character_name_slug).filter(stat_type="Type_1")
    type_2_statistics = Statistic.objects.filter(
            character__slug=character_name_slug).filter(stat_type="Type_2")
    type_3_statistics = Statistic.objects.filter(
            character__slug=character_name_slug).filter(stat_type="Type_3")
    type_4_statistics = Statistic.objects.filter(
            character__slug=character_name_slug).filter(stat_type="Type_4")

    if request.method == 'POST':

        form = StatisticForm(request.POST or None, character=character)

        if form.is_valid():
            statistic_character = character

            #for f in formset:
            cd = form.cleaned_data
            if cd.get('name') == None:
                pass
            else:
                name = cd.get('name')
                value = cd.get('value')
                s_type = cd.get('stat_type')
                statistic = Statistic(
                    name=name, value=value, character=statistic_character, stat_type=s_type)

                statistic.save()
                form = StatisticForm(character=character)

            HttpResponseRedirect("")

        else:
            print (form.errors)

    else:
        form = StatisticForm(character=character)

    return render(request, 'personas/add_statistics.html', {'form': form,
        'slug': character_name_slug, 'character': character,
        'type_1_statistics': type_1_statistics, 'type_2_statistics': type_2_statistics,
        'type_3_statistics': type_3_statistics, 'type_4_statistics': type_4_statistics,
        'story':story})


@login_required
def add_combat_info(request, character_name_slug):

    combat_info_list = CombatInfo.objects.filter(character__slug=character_name_slug)

    character = Character.objects.get(slug=character_name_slug)

    story = character.story

    if request.method == 'POST':

        form = CombatInfoForm(request.POST or None)

        if form.is_valid():
            combat_info_character = character

            cd = form.cleaned_data
            if cd.get('title') == None:
                pass
            else:
                title = cd.get('title')
                data = cd.get('data')
                combat_info = CombatInfo(
                    title=title, data=data, character=combat_info_character)

                combat_info.save()
                form = CombatInfoForm()

            HttpResponseRedirect("")

        else:
            print (form.errors)

    else:
        form = CombatInfoForm()

    return render(request, 'personas/add_combat_info.html', {'form': form,
        'slug': character_name_slug, 'character': character, 'story':story,
        'combat_info':combat_info_list})


@login_required
def add_ability(request, character_name_slug):

    abilities = SpecialAbility.objects.filter(character__slug=character_name_slug)

    character = Character.objects.get(slug=character_name_slug)
    story = character.story

    if request.method == 'POST':

        ability_form = SpecialAbilityForm(request.POST)

        if ability_form.is_valid():

            ability_data = ability_form.cleaned_data

            if ability_data.get('name') == None:
                pass
            else:
                name = ability_data.get('name')
                description = ability_data.get('description')
                ability = SpecialAbility(
                    name=name, description=description, character=character)

                ability.save()
                ability_form = SpecialAbilityForm()

            HttpResponseRedirect("")

        else:
            print (ability_form.errors)

    else:
        ability_form = SpecialAbilityForm()

    return render(request, 'personas/add_ability.html', {
        'slug': character_name_slug, 'character': character,
        'abilities': abilities, 'story':story,
        'ability_form':ability_form})


@login_required
def add_relationships(request, character_name_slug):

    relationships = Relationship.objects.filter(Q(to_character__slug=character_name_slug) |
        Q(from_character__slug=character_name_slug))

    character = Character.objects.get(slug=character_name_slug)

    story = character.story
    data = {"from_character": character}

    if request.method == 'POST':

        relationship_form = RelationshipForm(request.POST or None)

        if relationship_form.is_valid():

            relationship_data = relationship_form.cleaned_data

            if relationship_data.get('to_character') == None:
                pass
            else:
                to_character = relationship_data.get('to_character')
                relationship_description = relationship_data.get('relationship_description')
                weight = relationship_data.get('weight')
                relationship_class = relationship_data.get('relationship_class')
                relationship = Relationship(
                    from_character=character,
                    to_character=to_character,
                    relationship_description=relationship_description,
                    relationship_class=relationship_class, weight=weight)

                relationship.save()
                relationship_form = RelationshipForm(story=story)

            
            relationship_form = RelationshipForm(story=story)

        else:
            print (relationship_form.errors)

    else:
        relationship_form = RelationshipForm(story=story)

    return render(request, 'personas/add_relationships.html', {
        'slug': character_name_slug, 'character': character, 'story':story,
        'relationships': relationships, 'relationship_form':relationship_form})


@login_required
def add_chapter(request, story_title_slug):

    story = Story.objects.get(slug=story_title_slug)

    chapters = Chapter.objects.filter(story__slug=story_title_slug).order_by("-number")

    characters = Character.objects.filter(story=story)

    if request.method == 'POST':

        chapter_form = ChapterForm(request.POST or None)

        if chapter_form.is_valid():

            chapter_data = chapter_form.cleaned_data

            if chapter_data.get('title') == None:
                pass
            else:
                title = chapter_data.get('title')
                number = chapter_data.get('number')
                chapter_description = chapter_data.get('description')
                chapter_slug = slugify(chapter_data.get('title'))
                chapter = Chapter(title=title, story=story, number=number,
                    description=chapter_description, slug=chapter_slug)

                chapter.save()
                chapter_form = ChapterForm()

            return HttpResponseRedirect("/personas/chapter/{}".format(chapter_slug))

        else:
            print (chapter_form.errors)

    else:
        chapter_form = ChapterForm()

    return render(request, 'personas/add_chapter.html', {
        'slug': story_title_slug, 'story':story,
        'chapters': chapters, 'chapter_form':chapter_form})


@login_required
def add_scene(request, story_title_slug):

    story = Story.objects.get(slug=story_title_slug)

    scenes = Scene.objects.filter(chapter__story__slug=story_title_slug).order_by("-number")

    characters = Character.objects.filter(story=story)

    if request.method == 'POST':

        scene_form = SceneForm(request.POST or None)

        if scene_form.is_valid():
            scene = scene_form.save(commit=False)
            scene.slug = slugify(scene.title)
            scene.save()
            scene_form.save_m2m()

            return HttpResponseRedirect("/personas/scene/{}".format(scene.slug))

        else:
            print (scene_form.errors)

    else:
        scene_form = SceneForm(story=story)

    return render(request, 'personas/add_scene.html', {
        'slug': story_title_slug, 'story':story, 'scenes': scenes,
        'scene_form':scene_form, 'characters':characters})


@login_required
def add_location(request, story_title_slug):


    story = Story.objects.get(slug=story_title_slug)

    locations = Location.objects.filter(story__slug=story_title_slug)

    if request.method == 'POST':

        location_form = LocationForm(request.POST, request.FILES)

        if location_form.is_valid():
            location = location_form.save(commit=False)
            location.creator = request.user
            location.story = story
            location.slug = slugify(location.name)
            location.save()
            #location_form.save_m2m()

            return HttpResponseRedirect("/personas/location/{}".format(location.slug))

        else:
            print (location_form.errors)

    else:
        location_form = LocationForm(story=story)

    return render(request, 'personas/add_location.html', {
        'slug': story_title_slug, 'story':story, 'locations': locations,
        'location_form':location_form})


@login_required
def add_organization(request, story_title_slug):

    story = Story.objects.get(slug=story_title_slug)

    organizations = Organization.objects.filter(location__story=story)

    if request.method == 'POST':

        organization_form = OrganizationForm(request.POST or None, request.FILES or None)

        if organization_form.is_valid():
            organization = organization_form.save(commit=False)
            organization.creator = request.user
            organization.slug = slugify(organization.name)
            organization.story = story
            organization.save()

            return HttpResponseRedirect("/personas/organization/{}".format(organization.slug))

        else:
            print (organization_form.errors)

    else:
        organization_form = OrganizationForm(story=story)

    return render(request, 'personas/add_organization.html', {
        'slug': story_title_slug, 'story':story, 'organizations': organizations,
        'organization_form':organization_form})


@login_required
def add_nation(request, story_title_slug):

    story = Story.objects.get(slug=story_title_slug)

    nations = Nation.objects.filter(location__story=story)

    if request.method == 'POST':

        nation_form = NationForm(request.POST, request.FILES or None, story=story)

        if nation_form.is_valid():
            nation = nation_form.save(commit=False)
            nation.story = story
            nation.slug = slugify(nation.name)
            nation.save()

            return HttpResponseRedirect("/personas/nation/{}".format(nation.slug))

        else:
            print (nation_form.errors)

    else:
        nation_form = NationForm(story=story)

    return render(request, 'personas/add_nation.html', {
        'slug': story_title_slug, 'story':story, 'nations': nations,
        'nation_form':nation_form})



@login_required
def add_membership(request, character_name_slug):

    character = Character.objects.get(slug=character_name_slug)

    story = Story.objects.get(character=character)

    memberships = Membership.objects.filter(character=character)

    if request.method == 'POST':

        membership_form = MembershipForm(request.POST or None)

        if membership_form.is_valid():
            membership = membership_form.save(commit=False)
            membership.character = character
            membership.save()

            return HttpResponseRedirect("/personas/character/{}".format(character.slug))

        else:
            print (membership_form.errors)

    else:
        membership_form = MembershipForm(story=story)

    return render(request, 'personas/add_membership.html', {
        'slug': character_name_slug, 'story':story, 'memberships': memberships,
        'membership_form':membership_form, 'character': character})


@login_required
def add_artifact(request, slug, *args, **kwargs):

    try:
        story = Story.objects.get(slug=slug)
        character = None
    except ObjectDoesNotExist:
        character = Character.objects.get(slug=slug)
        story = Story.objects.get(character=character)

    artifacts = Item.objects.filter(story=story)

    if request.method == 'POST':

        artifact_form = ItemForm(request.POST, request.FILES or None)

        if artifact_form.is_valid():
            artifact = artifact_form.save(commit=False)
            artifact.slug = slugify(artifact.name)
            if character:
                artifact.character = character
            else:
                pass
            artifact.story = story
            artifact.save()

            return HttpResponseRedirect("")

        else:
            print (artifact_form.errors)

    else:
        artifact_form = ItemForm()

    return render(request, 'personas/add_artifact.html', {
        'story':story, 'artifacts': artifacts,
        'artifact_form':artifact_form, 'character':character})


# Edit and Delete Views

@login_required
def delete_skill(request, pk, template_name='personas/delete_skill.html'):
    skill = Skill.objects.get(pk=pk)
    character = Character.objects.get(skill=skill)
    if request.method=='POST':
        skill.delete()
        return HttpResponseRedirect('/personas/character/{}/#skills'.format(character.slug))
    return render(request, template_name, {'object': skill})

@login_required
def edit_skill(request, pk, template_name='personas/edit_skill.html'):
    skill = Skill.objects.get(pk=pk)
    character = Character.objects.get(skill=skill)
    story = character.story
    form = SkillForm(request.POST or None, instance=skill, character=character)
    if form.is_valid():
        form.save()
        return TemplateResponse(request, 'personas/redirect_template.html',
         {'redirect_url':'/personas/character/{}/#skills'.format(character.slug)})
    return render(request, template_name, {'form': form, 'character': character,
        'skill': skill, 'story':story})


@login_required
def delete_combat_info(request, pk, template_name='personas/delete_combat_info.html'):
    combat_info = CombatInfo.objects.get(pk=pk)
    character = Character.objects.get(combatinfo=combat_info)
    if request.method=='POST':
        combat_info.delete()
        return HttpResponseRedirect('/personas/character/{}/#skills'.format(character.slug))
    return render(request, template_name, {'object': combat_info})

@login_required
def edit_combat_info(request, pk, template_name='personas/edit_combat_info.html'):
    combat_info = CombatInfo.objects.get(pk=pk)
    character = Character.objects.get(combatinfo=combat_info)
    story = character.story
    form = CombatInfoForm(request.POST or None, instance=combat_info)
    if form.is_valid():
        form.save()
        return TemplateResponse(request, 'personas/redirect_template.html',
         {'redirect_url':'/personas/character/{}/#combat'.format(character.slug)})
    return render(request, template_name, {'form': form, 'character': character,
        'combat_info': combat_info, 'story':story})


@login_required
def delete_relationship(request, pk, template_name='personas/delete_relationship.html'):
    relationship = Relationship.objects.get(pk=pk)
    character = Character.objects.get(from_character=relationship.from_character)
    if request.method=='POST':
        relationship.delete()
        return HttpResponseRedirect('/personas/character/{}/#details'.format(character.slug))
    return render(request, template_name, {'object': relationship})


@login_required
def edit_relationship(request, pk, template_name='personas/edit_relationship.html'):
    relationship = Relationship.objects.get(pk=pk)
    character = Character.objects.get(id=relationship.from_character_id)
    story = character.story
    form = RelationshipForm(request.POST or None, instance=relationship)
    if form.is_valid():
        form.save()
        return TemplateResponse(request, 'personas/redirect_template.html',
         {'redirect_url':'/personas/character/{}/#details'.format(
            character.slug)})
    return render(request, template_name, {'form': form, 'from_character':character,
        'relationship': relationship, 'story':story})


@login_required
def delete_statistic(request, pk, template_name='personas/delete_statistic.html'):
    statistic = Statistic.objects.get(pk=pk)
    character = Character.objects.get(statistic=statistic)
    if request.method=='POST':
        statistic.delete()
        return HttpResponseRedirect('/personas/character/{}/#abilities'.format(character.slug))
    return render(request, template_name, {'object': statistic})


@login_required
def edit_statistic(request, pk, template_name='personas/edit_statistic.html'):
    statistic = Statistic.objects.get(pk=pk)
    character = Character.objects.get(statistic=statistic)
    story = character.story
    form = StatisticForm(request.POST or None, instance=statistic, character=character)
    if form.is_valid():
        form.save()
        return TemplateResponse(request, 'personas/redirect_template.html',
         {'redirect_url':'/personas/character/{}/#abilities'.format(character.slug)})
    return render(request, template_name, {'form': form, 'character':character,
        'statistic': statistic, 'story':story})


@login_required
def delete_ability(request, pk, template_name='personas/delete_ability.html'):
    specialability = SpecialAbility.objects.get(pk=pk)
    character = Character.objects.get(specialability=specialability)
    if request.method=='POST':
        specialability.delete()
        return HttpResponseRedirect('/personas/character/{}/#abilities'.format(character.slug))
    return render(request, template_name, {'object': specialability})


@login_required
def edit_ability(request, pk, template_name='personas/edit_ability.html'):
    specialability = SpecialAbility.objects.get(pk=pk)
    character = Character.objects.get(specialability=specialability)
    story = character.story
    form = SpecialAbilityForm(request.POST or None, instance=specialability)
    if form.is_valid():
        form.save()
        return TemplateResponse(request, 'personas/redirect_template.html',
         {'redirect_url':'/personas/character/{}/#abilities'.format(character.slug)})
    return render(request, template_name, {'form': form, 'character': character,
        'ability': specialability, 'story':story})


@login_required
def delete_trait(request, pk, template_name='personas/delete_trait.html'):
    trait = Trait.objects.get(pk=pk)
    character = Character.objects.get(trait=trait)
    if request.method=='POST':
        trait.delete()
        return HttpResponseRedirect('/personas/character/{}/#details'.format(character.slug))
    return render(request, template_name, {'object': trait})


@login_required
def edit_trait(request, pk, template_name='personas/edit_trait.html'):
    trait = Trait.objects.get(pk=pk)
    character = Character.objects.get(trait=trait)
    story = character.story
    form = TraitForm(request.POST or None, instance=trait)
    if form.is_valid():
        form.save()
        return TemplateResponse(request, 'personas/redirect_template.html',
         {'redirect_url':'/personas/character/{}/#details'.format(character.slug)})
    return render(request, template_name, {'form': form, 'character':character, 'trait': trait,
        'story':story})


@login_required
def delete_character(request, pk, template_name='personas/delete_character.html'):
    character = Character.objects.get(pk=pk)
    if request.method=='POST':
        character.delete()
        return HttpResponseRedirect('/personas/')
    return render(request, template_name, {'object': character})


@login_required
def edit_character(request, pk, template_name='personas/edit_character.html'):
    character = Character.objects.get(pk=pk)
    story = character.story
    user = request.user
    form = CharacterForm(request.POST or None, request.FILES or None, instance=character)
    if form.is_valid():
        form.save(creator=character.creator, story=story)
        return HttpResponseRedirect('/personas/character/{}'.format(character.slug))
    return render(request, template_name, {'form': form, 'character':character,
        'story':story})


@login_required
def delete_story(request, pk, template_name='personas/delete_story.html'):
    story = Story.objects.get(pk=pk)
    if request.method=='POST':
        story.delete()
        return HttpResponseRedirect('/personas/')
    return render(request, template_name, {'object': story})


@login_required
def edit_story(request, pk, template_name='personas/edit_story.html'):
    story = Story.objects.get(pk=pk)
    user = request.user
    form = StoryForm(request.POST or None, request.FILES or None, instance=story)
    if form.is_valid():
        form.save(author=story.author)
        return HttpResponseRedirect('/personas/story/{}'.format(story.slug))
    return render(request, template_name, {'form': form, 'story':story})


@login_required
def delete_location(request, pk, template_name='personas/delete_location.html'):
    location = Location.objects.get(pk=pk)
    story = Story.objects.get(location=location)
    if request.method=='POST':
        location.delete()
        return HttpResponseRedirect('/personas/{}'.format(story.slug))
    return render(request, template_name, {'object': location})


@login_required
def edit_location(request, pk, template_name='personas/edit_location.html'):
    location = Location.objects.get(pk=pk)
    story = location.story
    user = request.user
    form = LocationForm(request.POST or None, request.FILES or None, instance=location)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/personas/location/{}'.format(location.slug))
    return render(request, template_name, {'form': form, 'location':location, 'story':story})


@login_required
def delete_organization(request, pk, template_name='personas/delete_organization.html'):
    organization = Organization.objects.get(pk=pk)
    story = Story.objects.get(organization=organization)
    if request.method=='POST':
        organization.delete()
        return HttpResponseRedirect('/personas/{}'.format(story.slug))
    return render(request, template_name, {'object': organization})


@login_required
def edit_organization(request, pk, template_name='personas/edit_organization.html'):
    organization = Organization.objects.get(pk=pk)
    story = organization.story
    user = request.user
    form = OrganizationForm(request.POST or None, request.FILES or None, instance=organization)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/personas/organization/{}'.format(organization.slug))
    return render(request, template_name, {'form': form, 'organization':organization, 'story':story})


@login_required
def delete_chapter(request, pk, template_name='personas/delete_chapter.html'):
    chapter = Chapter.objects.get(pk=pk)
    story = Story.objects.get(chapter=chapter)
    if request.method=='POST':
        chapter.delete()
        return HttpResponseRedirect('/personas/story/{}'.format(story.slug))
    return render(request, template_name, {'object': chapter})


@login_required
def edit_chapter(request, pk, template_name='personas/edit_chapter.html'):
    chapter = Chapter.objects.get(pk=pk)
    story = chapter.story
    user = request.user
    form = ChapterForm(request.POST or None, request.FILES or None, instance=chapter)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/personas/chapter/{}'.format(chapter.slug))
    return render(request, template_name, {'form': form, 'object':chapter, 'story':story})


@login_required
def delete_scene(request, pk, template_name='personas/delete_scene.html'):
    scene = Scene.objects.get(pk=pk)
    story = Story.objects.get(chapter__scene=scene)
    if request.method=='POST':
        scene.delete()
        return HttpResponseRedirect('/personas/story/{}'.format(story.slug))
    return render(request, template_name, {'object': scene})


@login_required
def edit_scene(request, pk, template_name='personas/edit_scene.html'):
    scene = Scene.objects.get(pk=pk)
    user = request.user
    story = Story.objects.get(chapter__scene=scene)
    form = SceneForm(request.POST or None, request.FILES or None, instance=scene, story=story)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/personas/scene/{}'.format(scene.slug))
    return render(request, template_name, {'form': form, 'object':scene, 'story':story})


@login_required
def delete_membership(request, pk, template_name='personas/delete_membership.html'):
    membership = Membership.objects.get(pk=pk)
    character = membership.character
    if request.method=='POST':
        membership.delete()
        return HttpResponseRedirect('/personas/character/{}/#details'.format(character.slug))
    return render(request, template_name, {'object': membership})


@login_required
def edit_membership(request, pk, template_name='personas/edit_membership.html'):
    membership = Membership.objects.get(pk=pk)
    character = membership.character
    story = character.story
    form = MembershipForm(request.POST or None, instance=membership)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/personas/character/{}/#details'.format(character.slug))
    return render(request, template_name, {'form': form, 'character':character, 'membership': membership,
        'story':story})


@login_required
def delete_artifact(request, pk, template_name='personas/delete_artifact.html'):
    artifact = Item.objects.get(pk=pk)
    character = Character.objects.get(item=artifact)
    if request.method=='POST':
        artifact.delete()
        return HttpResponseRedirect('/personas/character/{}/#abilities'.format(character.slug))
    return render(request, template_name, {'object': artifact})


@login_required
def edit_artifact(request, pk, template_name='personas/edit_artifact.html'):
    artifact = Item.objects.get(pk=pk)
    character = Character.objects.get(item=artifact)
    story= character.story
    form = ItemForm(request.POST or None, instance=artifact)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/personas/character/{}/#abilities'.format(character.slug))
    return render(request, template_name, {'form': form, 'character':character, 'artifact': artifact, 'story':story})


@login_required
def delete_nation(request, pk, template_name='personas/delete_nation.html'):
    nation = Nation.objects.get(pk=pk)
    story = Story.objects.get(nation=nation)
    if request.method=='POST':
        nation.delete()
        return HttpResponseRedirect('/personas/{}'.format(story.slug))
    return render(request, template_name, {'object': nation})


@login_required
def edit_nation(request, pk, template_name='personas/edit_nation.html'):
    nation = Nation.objects.get(pk=pk)
    story = Story.objects.get(nation=nation)
    user = request.user
    form = NationForm(request.POST or None, request.FILES or None, instance=nation)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/personas/nation/{}'.format(nation.slug))
    return render(request, template_name, {'form': form, 'nation':nation, 'story':story})

