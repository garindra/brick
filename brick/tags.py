from .utils import make_tag, text

_tags_to_build = ('A', 'Div', 'Span', 'Script', 'Link', 'Title', 'Head', 'Body', 
                  'Html', 'Head', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'P', 'Meta',
                  'Textarea', 'Form', 'Ul', 'Ol', 'Li', 'Code', 'Blockquote', 'Em', 
                  'Strong', 'Select', 'Option', 'Iframe')

_self_closing_tags_to_build = ('Input', 'BR', 'Img')

for tag in _tags_to_build:
    #define the tag in the current module
    vars()[tag] = make_tag(tag)

for tag in _self_closing_tags_to_build:
    #define the tag in the current module
    vars()[tag] = make_tag(tag, self_closing=True)
