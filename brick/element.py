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
                result = self._process_buffer(self.after_render_buffer(self.render_buffer()))
        else:
            result = self._process_buffer(self.after_render_buffer(self.render_buffer()))

        return result

    def _process_buffer(self, buf):
        
        self.before_process_buffer(buf)

        #If self.render returns nothing, then just return empty string
        if buf is None:
            return ""

        #If the result is a string, then just directly return that
        if isinstance(buf, str):
            return buf 
        
        #If the result is an instance of Element, then call the render_buffer method of it.
        #And return that.
        if isinstance(buf, Element):
            return buf.render()

        if isinstance(buf, list):
            return self._merge_buffer(buf)
        
    def _merge_buffer(self, buf):
        temp_buf = []

        for element in buf:

            if isinstance(element, Element):
                temp_buf.append(element.render())

            elif isinstance(element, str):
                temp_buf.append(element)

            else:
                raise Exception("Only Element or str instance are allowed in render")

        return ''.join(temp_buf)

    def render_buffer(self):
        """ 
            Implementing the render method is simple; return a string, a list
            of strings, or an instance of Element subclass.
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
