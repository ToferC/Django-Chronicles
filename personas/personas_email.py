from django.core.mail import send_mail, EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template
import datetime



def mail_format(s_object, s_object_name, note_creator, title, content,
    noun="note", verb="added"):

    try:
        to_email = s_object.creator.email
        creator = s_object.creator
    except AttributeError:
        to_email = s_object.author.email
        creator = s_object.author

    if s_object.__class__.__name__ == 'StoryObject':
        so_type = "storyobject"
    elif s_object.__class__.__name__ == 'Location':
        so_type = "location"
    elif s_object.__class__.__name__ == 'Chapter':
        so_type = "chapter"
    elif s_object.__class__.__name__ == 'Scene':
        so_type = "scene"
    elif s_object.__class__.__name__ == 'Nation':
        so_type = "nation"
    else:
        so_type = "story"

    subject = "Personas Notification: A new {noun} has been {verb} to {subject}".format(
        noun=noun,
        verb=verb,
        subject=s_object_name)

    from_email = 'personas.story@gmail.com'
    ctx = {
        'creator': creator,
        'note_creator': note_creator,
        'noun': noun,
        'verb': verb,
        's_object': s_object,
        'title': title,
        'content': content,
        'date': datetime.date.today(),
        'so_type': so_type,
        'slug': s_object.slug
    }

    message = get_template('personas/email.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=[to_email], from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()