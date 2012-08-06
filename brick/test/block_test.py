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
