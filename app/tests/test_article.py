import unittest
from app.models import Articles



class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles(John, Never Give up, Encouragement, "https: // visual.ly/community/Infographics/business/what-planned-bitcoin-2020", "https: // thumbnails-visually.netdna-ssl.com/what-is-planned-for-bitcoin-in-2020_5f021162d20dd_w250_h250.png", 2020-07-05T17: 44: 02Z", WHAT IS PLANNED FOR BITCOIN IN 2020? BITCOIN WAS INTRODUCED IN THE YEAR 2009. IT WAS LAUNCHED UNDER THE GROUP NAMED SATOSHI NAKAMOTO. 1 TOM LEE 2020 PREDICTION Tom Lee is the co-founder of the firm F… [+1465 chars])

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))
