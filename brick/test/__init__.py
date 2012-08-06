import unittest

import brick
from brick.utils import make_tag

class BrickTextTestCase(unittest.TestCase):
    
    def setUp(self):
        self.text = brick.Text("awesome")

    def test_render_buffer(self):

        text_contents = self.text.render_buffer()
        self.assertEqual(text_contents, "awesome")
