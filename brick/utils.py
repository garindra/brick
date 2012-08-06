import tag
from .text import Text

def make_tag(cls_name, tag_name=None, self_closing=False):
    """
    
        Dynamically creates new subclasses of Tag.

        Example usage:

        Div = make_tag('div', self_closing=True)
        
    """
    if tag_name is None:
        tag_name = cls_name.lower()
    
    return type(cls_name, (tag.Tag,), {

        'tag_name' : tag_name,
        'self_closing' : self_closing
    })

def text(string):
    return Text(string)

def is_context_manager(obj):
    return callable(getattr(obj, '__enter__', None))\
                    and callable(getattr(obj, '__exit__', None))
