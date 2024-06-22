import logging
from typing import List

from .core import ScraperAPI

logger = logging.getLogger(__name__)


class Instagram(ScraperAPI):
    base_url = "https://api.brightdata.com"

    async def posts(self, urls: List[str]):
        DATASET_ID = "gd_lk5ns7kz21pck8jpis"
        return await self.collect(dataset_id=DATASET_ID, payload=[{"url": url} for url in urls])

    async def comments(self, urls: List[str]):
        DATASET_ID = "gd_ltppn085pokosxh13"
        return await self.collect(dataset_id=DATASET_ID, payload=[{"url": url} for url in urls])

    async def profiles(self, urls: List[str]):
        DATASET_ID = "gd_l1vikfch901nx3by4"
        return await self.collect(dataset_id=DATASET_ID, payload=[{"url": url} for url in urls])
