class Element(object):
    """
        Element is the base class for three main Brick classes: Tag, Block,
        and Text.
    """
    def __iter__(self):
        yield self

    def __str__(self):
        return self.render_buffer()

    def render_buffer(self):
        """ 
            
            render_buffer is the method that external objects should call
            to get the actual "contents" of the element.

            What render_buffer does is basically calling the `render` method
            that should be implemented by the subclasses.

            The `render` method can return a single string or a list of strings.
            If it happens to be a list of strings, then it is the task of the
            `render_buffer` to merge them into a single string and return them.

        """
        
        context_manager = self.before_render()

        if utils.is_context_manager(context_manager):
            with context_manager:
                result = self._process_buffer(self.after_render(self.render()))
        else:
            result = self._process_buffer(self.after_render(self.render()))

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
            return buf.render_buffer()

        if isinstance(buf, list):
            return self._merge_buffer(buf)
        
    def _merge_buffer(self, buf):
        temp_buf = []

        for element in buf:

            if isinstance(element, Element):
                temp_buf.append(element.render_buffer())

            elif isinstance(element, str):
                temp_buf.append(element)

            else:
                raise Exception("Only Element or str instance are allowed in render_buffer")

        return ''.join(temp_buf)

    def render(self):
        """ 
            Implementing the render method is simple; return a string, a list
            of strings, or an instance of Element subclass.
        """
        raise NotImplementedError("`render` method should be implemented for %s" % (
                                    self.__class__.__name__))
    
    def before_render(self):
        """

        """
        pass

    def after_render(self, buf):
        """
            `after_render` is a method that's called
        """
        return buf

    def before_process_buffer(self, buf):
        return buf

    def after_process_buffer(self, buf):
        return buf

import utils
