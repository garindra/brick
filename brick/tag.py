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
        
        buf.append(self.get_opening_tag_str())
        buf.append(self.content)
        buf.append(self.get_closing_tag_str())

        return buf

    def __call__(self, content, escape=False):

        if self.self_closing:
            raise exceptions.SelfClosingTagWithContentException("Self-closing tag should not have content")

        self.content = cgi.escape(content) if escape else content

        return self

    def __enter__(self):

        if self.content is not None:
            raise exceptions.WrappingTagWithContentException(
                                        "Wrapping tag should not have content.")

        self.buf += self.get_opening_tag_str()

    def __exit__(self, type, value, traceback):
        self.buf += self.get_closing_tag_str()

    def into(self, buf):
        self.buf = buf

        return self

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

    def get_opening_tag_str(self):
        return '<' + self.tag_name + self._print_attrs() + ('/>' if self.self_closing else '>')

    def get_closing_tag_str(self):
        return '</' + self.tag_name + '>'

    def _print_attrs(self):
        attrs_str = ''

        for key, value in self._kwargs.items():

            if key == 'class_':
                key = 'class'
            else:
                key = key.replace('_', '-')

            if isinstance(value, list):
                value = ' '.join(value)

            attrs_str += (' ' + key + '="' + str(value) + '"')
            
        return attrs_str

