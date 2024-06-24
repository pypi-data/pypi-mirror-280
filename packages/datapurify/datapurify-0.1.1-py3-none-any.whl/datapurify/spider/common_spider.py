from datapurify.spider.spider import Spider
from playwright.async_api import async_playwright, Playwright
from playwright.sync_api import sync_playwright, Playwright
from datapurify.base import Document


class CommonSpider(Spider):

    def __init__(self):
        pass

    def crawl(self, url: str):
        with sync_playwright() as playwright:
            webkit = playwright.webkit
            browser = webkit.launch()
            page = browser.new_page()
            js = """
                    Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
                    """
            page.add_init_script(js)
            page.goto(url)
            page.wait_for_load_state('networkidle', timeout=3000)
            html = page.content()
            browser.close()
            document = Document(url=url, metadata={}, page_content=html)
            return document

    async def a_crawl(self, surl: str):
        pass
