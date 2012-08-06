import element

class Text(element.Element):
    """
        A regular HTML text node.
    """
    
    def __init__(self, content):
        self.content = content

    def render_buffer(self):
        return self.content
