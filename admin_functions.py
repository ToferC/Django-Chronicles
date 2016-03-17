# File for various admin functions

def return_object(s_object):
    # retrieve object type function

    if s_object.__class__.__name__ == 'StoryObject':
        so_type = "storyobject"
    elif s_object.__class__.__name__ == 'Place':
        so_type = "place"
    elif s_object.__class__.__name__ == 'Chapter':
        so_type = "chapter"
    elif s_object.__class__.__name__ == 'Scene':
        so_type = "scene"
    elif s_object.__class__.__name__ == 'Nation':
        so_type = "nation"
    else:
        so_type = "story"

    return so_type