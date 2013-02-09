from __future__ import with_statement

import unittest

import brick
from brick.tags import A, Div
from brick.utils import text
from brick.exceptions import WrappingTagWithContentException

class BlockTestCase(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_empty_block(self):

        block = EmptyBlock()
        self.assertEqual(block.render(), "")

    def test_block_with_single_tag(self):
        
        block = SingleTagBlock()
        self.assertEqual(block.render(), "<a>I am a lonely link tag.</a>")

    def test_block_with_multiple_tags(self):

        block = MultipleTagsBlock()

        render_result = block.render()
        target_result = "<a>first</a><a>second</a><a>third</a>"

        self.assertEqual(render_result, target_result)

    def test_block_with_multilevel_tags(self):

        block = MultiLevelTagsBlock()

        render_result = block.render()
        target_result = '<div><div><a>content</a></div></div>'

        self.assertEqual(render_result, target_result)
        

    def test_multilevel_block(self):
        
        block = FirstLevelBlock()
        self.assertEqual(block.render(), "<div>first<div>second</div></div>")

    def test_wrapping_tag_exception_raising(self):
        block = WrappingTagWithContentExceptionRaisingBlock()

        self.assertRaises(WrappingTagWithContentException, block.render_buffer)

    def test_after_construct(self):
        
        block = ModifyingAfterConstructBlock()

        target_result = '<div id="wrapping-div"><div>original content</div></div>'

        self.assertEqual(block.render(), target_result)

    def test_before_construct_context_manager(self):
        
        block = BlockWithContextManager()

        block.render()

        self.assertEqual(block.test_context_manager.enter_method_is_run, True)
        self.assertEqual(block.test_context_manager.exit_method_is_run, True)

    def test_context_manager_multiple_level(self):
        
        class RootBlock(brick.Block):
            
            def construct(self):
                
                b = []

                for i in xrange(2):
                    b += BranchBlock(1, i, 0)

                return b

        class BranchBlock(brick.Block):

            def __init__(self, level, index, parent_index):
                
                self.level = level
                self.index = index
                self.parent_index = parent_index

                self.batch()

            #def before_construct(self):
            #    return BranchContextManager()

            def batch(self):
                #print "%s:%s:%s" % (self.level, self.index, self.parent_index)
                pass

            def construct(self):

                print "%s:%s:%s" % (self.level, self.index, self.parent_index)

                b = []

                if self.level < 2:
                    for i in xrange(2):
                        b += BranchBlock(self.level + 1, i, self.index)

                return b

        class Cacher(object):
            pass

        class Batcher(object):
            pass

        class BranchContextManager():

            def __init__(self):
                pass
            
            def __enter__(self):
                pass
            
            def __exit__(self, type, value, traceback):
                pass

        root_block = RootBlock()

        print root_block.render()

class EmptyBlock(brick.Block):
    
    def construct(self):
        pass

class SingleTagBlock(brick.Block):
    
    def construct(self):
        return A()("I am a lonely link tag.")

class MultipleTagsBlock(brick.Block):
    
    def construct(self):
        
        z = []

        z += A()("first")
        z += A()("second")
        z += A()("third")

        return z

class WrappingTagWithContentExceptionRaisingBlock(brick.Block):
    
    def construct(self):
        z = []

        with Div()("content").into(z):
            z += A("link")

        return z

class MultiLevelTagsBlock(brick.Block):
    
    def construct(self):
        
        z = []

        with Div().into(z):
            with Div().into(z):
                z += A()("content")

        return z

class FirstLevelBlock(brick.Block):
    
    def construct(self):    
        z = []

        with Div().into(z):
            z += text("first")
            z += SecondLevelBlock()

        return z

class SecondLevelBlock(brick.Block):
    
    def construct(self):
        z = []

        with Div().into(z):
            z += text("second")

        return z

class ModifyingAfterConstructBlock(brick.Block):
    
    def construct(self):
        return Div()("original content") 

    def after_construct(self, result):
        z = []

        with Div(id="wrapping-div").into(z):
            z += result

        return z

class MultipleSectionBlock(brick.Block):

    def construct(self):

        z = []
        
        with Div().into(z):
            z += self.declare_section('left')

        with Div().into(z):
            z += self.declare_section('right')

        return z

class MultipleSectionTestBlock(brick.Block):
    
    def construct(self):
        
        with MultipleSectionBlock().into(z) as layout:
            
            with layout.left as z:
                pass

            with layout_get_section('right'):
                pass

        return z

class BlockWithContextManager(brick.Block):
    
    def before_construct(self):
        self.test_context_manager = TestBlockContextManager()

        return self.test_context_manager

    def construct(self):
        pass

class TestBlockContextManager(object):
    
    def __enter__(self):
        self.enter_method_is_run = True

    def __exit__(self, type, value, traceback):
        self.exit_method_is_run = True
