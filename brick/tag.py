import cgi

import element
import exceptions

class Tag(element.Element):
    
    self_closing = False
    content = None

    def __init__(self, *args, **kwargs):
        
        self._args = args
        self._kwargs = kwargs
    
    def render_buffer(self):   
        
        buf = []
        
        buf.append('<' + self.tag_name + self._print_attrs())

        if self.self_closing:
            buf.append('/>')

        else:
            buf.append('>')
            buf.append(self.content)
            buf.append('</' + self.tag_name + '>')

        return buf

    def __call__(self, content, escape=False):

        self.content = cgi.escape(content) if escape else content

        return self

    def __enter__(self):

        if getattr(self, 'content', None):
            raise exceptions.WrappingTagWithContentException("Wrapping tag should not have content.")

        self.z += '<' + self.tag_name + self._print_attrs() + '>' 

    def __exit__(self, type, value, traceback):
        self.z += '</' + self.tag_name + '>'  

    def into(self, z):
        self.z = z

        return self

    def _print_attrs(self):
        attrs_str = ''

        for key, value in self._kwargs.items():

            if key == 'class_':
                key = 'class'

            if isinstance(value, list):
                value = ' '.join(value)

            attrs_str += (' ' + key + '="' + str(value) + '"')
            
        return attrs_str

    def add_attribute(self, key, value):
        self._kwargs[key] = value

    def remove_attribute(self, key):
        del self._kwargs[key]

    def __setitem__(self, key, value):
        self.add_attribute(key, value)

    def __delitem__(self, key):
        self.remove_attribute(key)

    def set_content(self, content):
        self.content = content
