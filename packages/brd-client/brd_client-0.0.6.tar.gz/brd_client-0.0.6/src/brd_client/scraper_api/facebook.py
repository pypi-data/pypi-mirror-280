import logging
from typing import List

from .core import ScraperAPI

logger = logging.getLogger(__name__)


class Facebook(ScraperAPI):
    base_url = "https://api.brightdata.com"

    async def posts(self, urls: List[str], days_range: int = 30, num_of_posts: int = 100):
        DATASET_ID = "gd_lkaxegm826bjpoo9m5"
        return await self.collect(
            dataset_id=DATASET_ID,
            payload=[{"url": url, "days_range": days_range, "num_of_posts": num_of_posts} for url in urls],
        )

    async def comments(self, urls: List[str]):
        DATASET_ID = "gd_lkay758p1eanlolqw8"
        return await self.collect(dataset_id=DATASET_ID, payload=[{"url": url} for url in urls])

    async def profiles(self, urls: List[str]):
        raise NotImplementedError("Bright Data는 아직 Facebook Profile에 대한 Scraper API 기능을 제공하지 않음!")
