import unittest
from models import news,articles

Article = articles.Article

class NewsTest(unittest.TestCase):

    def setUp(self):
        self.new_source = Article('self','associated_press','Associated Press','Cant crush this: Beetle armor gives clues to tougher planes','http://apnnews.com"','https://storage.googleapis.com/afs-prod/media/7de42fed748f448883a9ae11391ef2c0/2532.jpeg,'2020-10-21T18:01:29Z')
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
        self.assertEquals(self.new_origin.author,'Bloomberg')
        self.assertEquals(self.new_origin.title,'Bloomberg delivers business and markets news')
        self.assertEquals(self.new_origin.description,"http://www.bloomberg.com")
        self.assertEquals(self.new_origin.url,'business')
        self.assertEquals(self.new_origin.image,'en')
        self.assertEquals(self.new_origin.date,'us')
        
    
if __name__ == '__main__':
    unittest.main()

