from abc import ABC


class Spider(ABC):

    def crawl(self, surl: str):
        raise NotImplementedError

    async def a_crawl(self, surl: str):
        raise NotImplementedError
