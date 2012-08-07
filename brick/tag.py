import element
import exceptions

class Tag(element.Element):
    
    self_closing = False

    def __init__(self, *args, **kwargs):
        
        self._args = args
        self._kwargs = kwargs
    
    def render_buffer(self):   
        #content could be a string or list
        content = getattr(self, '_content', '')
        
        #if it's a list, then let's join it into a complete string
        if isinstance(content, list):
            content = self._merge_buffer(content)

        elif content is None:
            content = ""

        if self.self_closing:
            return '<' + self.tag_name + self._print_attrs() + '/>' 
        else:
            return '<' + self.tag_name + self._print_attrs() + '>' + (str(content) or '') + '</' + self.tag_name + '>'

    def __call__(self, content):
        self._content = content

        return self

    def __enter__(self):

        if getattr(self, '_content', None):
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
        self._content = content
