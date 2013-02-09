from __future__ import with_statement

class Element(object):
    """
        Element is the base class for three main Brick classes: Tag, Block,
        and Text.
    """
    def __iter__(self):
        yield self

    def __str__(self):
        return self.render()

    def render(self):
        """ 
            
            `render` is the method that external objects should call
            to get the actual "contents" of the element.

            What render does is basically calling the `render_buffer` method
            that should be implemented by the subclasses.

            The `render_buffer` method can return a single string or a list of strings.
            If it happens to be a list of strings, then it is the task of the
            `render` to merge them into a single string and return them.

        """
        
        context_manager = self.before_render_buffer()

        if utils.is_context_manager(context_manager):
            with context_manager:
                result = self.process_buffer(self.after_render_buffer(self.render_buffer()))
        else:
            result = self.process_buffer(self.after_render_buffer(self.render_buffer()))

        return result
    
    def process_buffer(self, buf):
        
        return self.after_process_buffer(self._process_buffer(
                                            self.before_process_buffer(buf)))

    def _process_buffer(self, buf):
        
        #If self.render returns nothing, then just return empty string
        if buf is None:
            return ""

        #If the result is a string, then just directly return that
        elif isinstance(buf, str):
            return buf 
        
        #If the result is an instance of Element, then call the render_buffer method of it.
        #And return that.
        elif isinstance(buf, Element):
            return buf.render()

        elif isinstance(buf, list):
            return "".join(map(self._process_buffer, buf))

        else:
            raise Exception("Only Element or str instance are allowed in render")

    def render_buffer(self):
        """ 
            Implementing the render method is simple; return a string, a list
            of strings, or instances of Element subclass.
        """
        raise NotImplementedError("`render_buffer` method should be implemented for %s" % (
                                    self.__class__.__name__))
    
    def before_render_buffer(self):
        """

        """
        pass

    def after_render_buffer(self, buf):
        """
        
        """
        return buf

    def before_process_buffer(self, buf):
        return buf

    def after_process_buffer(self, buf):
        return buf

import utils
