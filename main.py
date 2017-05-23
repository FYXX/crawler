
# coding: utf-8

# In[ ]:

from icrawler.builtin import GreedyImageCrawler
greedy_crawler = GreedyImageCrawler(parser_threads=2, downloader_threads=2,storage={'root_dir': 'data'})
greedy_crawler.crawl(domains='www.***.com', max_num=1000, min_size=None, max_size=None)


# In[ ]:

from icrawler.builtin import BaiduImageCrawler
baidu_crawler = BaiduImageCrawler(storage={'root_dir': 'data'})
baidu_crawler.crawl(keyword='猫',offset=0, max_num=1000,min_size=None, max_size=None)


# In[ ]:

from icrawler.builtin import GoogleImageCrawler
Google_Crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=2, storage={'root_dir': 'data'})
Google_Crawler.crawl(keyword='flower', max_num=1000, date_min=None, date_max=None, min_size=(160,160), max_size=None)

