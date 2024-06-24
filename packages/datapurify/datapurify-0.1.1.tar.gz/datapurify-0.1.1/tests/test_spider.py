from datapurify.spider.common_spider import CommonSpider


def test_common_spider():
    spider = CommonSpider()
    doc = spider.crawl("https://baike.baidu.com/item/%E9%87%91%E7%BC%95%E7%8E%89%E8%A1%A3/617831?fr=ge_ala")
    print(doc)
