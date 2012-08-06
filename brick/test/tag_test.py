import unittest

from brick.utils import make_tag

class BrickTagTestCase(unittest.TestCase):
    
    def setUp(self):
        
        self.tag_cls = make_tag("A")

    def test_make_tag(self):
        #Should have the correct tag name
        self.assertEqual(self.tag_cls.tag_name, "a")

    def test_render_without_attributes_or_content(self):
        
        tag = self.tag_cls()
        self.assertEqual(tag.render_buffer(), "<a></a>")

    def test_render_with_attribute(self):
        
        tag = self.tag_cls(id="test-id")

        self.assertEqual(tag.render_buffer(), '<a id="test-id"></a>')

    def test_render_with_class_attribute(self):
        
        tag = self.tag_cls(class_=['bold', 'medium'])

        self.assertEqual(tag.render_buffer(), '<a class="bold medium"></a>')
    
    def test_render_with_content(self):
        
        tag = self.tag_cls()("This is a link tag")
        self.assertEqual(tag.render_buffer(), '<a>This is a link tag</a>')

    def test_render_with_content_and_attributes(self):
        
        tag = self.tag_cls(href="#")("This is a link tag")
        self.assertEqual(tag.render_buffer(), '<a href="#">This is a link tag</a>')

    def test_adding_and_removing_attributes_after_init(self):
        tag = self.tag_cls(id="myid")

        tag.add_attribute('href', '#')
        tag.remove_attribute('id')

        self.assertEqual(tag.render_buffer(), '<a href="#"></a>')

    def test_setting_content_after_init(self):
        
        tag = self.tag_cls()

        tag.set_content('content after init')

        self.assertEqual(tag.render_buffer(), '<a>content after init</a>')

    def test_setitem(self):
        
        tag = self.tag_cls()
        tag['id'] = 'testing-id'

        self.assertEqual(tag.render_buffer(), '<a id="testing-id"></a>')
