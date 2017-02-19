

import unittest
from news_spider import BbcSpider
from responses import fake_response_from_file

class NewsSpiderTest(unittest.TestCase):

    def setUp(self):
        self.crawler = Crawler(DefaultSpider, Settings())
        self.spider = self.crawler.spiders

    def _test_item_results(self, results, expected_length):
        count = 0
        permalinks = set()
        for item in results:
            self.assertIsNotNone(item['content'])
            self.assertIsNotNone(item['title'])
            sself.assertEqual(count, expected_length)

    def test_parse(self):
        results = self.spider.parse(fake_response_from_file('osdir/sample.html'))
        self._test_item_results(results, 10)



if __name__ == '__main__':
    unittest.main()
