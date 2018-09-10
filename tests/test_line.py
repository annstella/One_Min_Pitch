import unittest
from app.models import Line,Group,User

class TestLine(unittest.TestCase):

    def setUp(self):

        self.new_line = Line( line_content="Nice scene over here")

    def test_instance(self):
        '''
        Test case to check if new_line is an instance of Line
        '''
        self.assertTrue( isinstance( self.new_line, Line) )

    def test_save_line(self):
        
        self.new_line.save_line()

        self.assertTrue( len(Line.query.all()) > 0)

    def test_get_lines(self):
        '''
        Test case to check if a line and its information is returned by the get_lines function that takes in an id and match it to id in the group table
        '''

        self.new_line.save_line()

        gotten_lines = Line.get_lines(4990826417581240726341234)

        self.assertFalse( len(gotten_lines) == 1)

    