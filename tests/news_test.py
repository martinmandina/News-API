import unittest
from app.models import Sources

Source = news.Sources

class NewsTest(unittest.TestCase):

    def setUp(self):
        self.new_source = Source('self','bloomberg','Bloomberg','Bloomberg delivers business and markets','http://www.bloomberg.com"','business','en','us')
        '''
        This method that will run before every Test
        '''

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_confirm_variable_instatiation(self):
        '''
        Test to confirm that objects are instaitated correctly
        '''
        self.assertEquals(self.new_origin.id,'bloomberg')
        self.assertEquals(self.new_origin.name,'Bloomberg')
        self.assertEquals(self.new_origin.description,'Bloomberg delivers business and markets news')
        self.assertEquals(self.new_origin.url,"http://www.bloomberg.com")
        self.assertEquals(self.new_origin.category,'business')
        self.assertEquals(self.new_origin.language,'en')
        self.assertEquals(self.new_origin.country,'us')
        
    
if __name__ == '__main__':
    unittest.main()

