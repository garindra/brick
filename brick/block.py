from __future__ import with_statement

from .element import Element
import utils

class Block(Element):
    """
        Block is the direct subclass of element; it allows users to 
        create a tree of Element subclasses (such as Nodes or Blocks themselves) 
        by implementing the construct method.
        
        Example:

        import brick
        from brick.tags import Div, A

        class LoginButton(brick.Block):
            
            def construct(self):
                
                z = []

                with Div(class_=['curved']).into(z):
                    z += A(href='/login')('Login')

                return z

    """
    
    def render_buffer(self):

        context_manager = self.before_construct()

        if utils.is_context_manager(context_manager):
            with context_manager:
                result = self.construct()
        else:
            result = self.construct()

        result = self.after_construct(result)
        
        return result
    
    def before_construct(self):
        """"
            
            The `before_construct` will be called right before we run the
            `construct` method. It allows the Block to do whatever it needs
            to do before constructing. You can return a context manager
            object and the `construct` method will be run inside the with block
            of that context manager.

        """
        pass

    def after_construct(self, result):
        """
            The `after_construct` method allows a subclass of Block to 
            modify/examine the result of the `construct` method before passing it 
            down to the `render_buffer` method. 

            Example uses of this would be to wrap whatever the result object
            of the render method with a DIV, for example.
        """
        return result

    def construct(self):
        raise NotImplementedError("The `construct` method should be" + 
                                    "implemented for Block subclass %s."
                                    % self.__class__.__name__)
