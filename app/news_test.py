import unittest
from models import news

News = news.News

class NewsTest(unittest.TestCase):

    def setUp(self):
        self.new_news = News('Rebecca Tan','Women March','Hundreds Gathered for march',
        'https://www.washingtonpost.com/dc-md-va/2020/10/17/womens-march-dc-updates',
        'https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/MAEO5TPCYNAVHF72H6LFACODXE.jpg&w=1440',
        '2020-10-17T16:23:00Z',
        'Everything we have been doing has been')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()

