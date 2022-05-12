import unittest

from app.models import Pitch


class TestModelPitch(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch('This is my new pitch', 'Morces', 0,0,0)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))