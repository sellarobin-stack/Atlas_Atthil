from __future__ import annotations

from app.data_pipeline.cache.cache_manager import CacheManager
from app.data_pipeline.sources import DofusDbClient


class QuestDownloader:

    CACHE_FILE = "quests.json"

    def __init__(
        self,
        cache: CacheManager,
    ):
        self.cache = cache

    def download(
        self,
        use_cache: bool = True,
    ) -> list[dict]:

        if use_cache and self.cache.exists(self.CACHE_FILE):
            return self.cache.load(self.CACHE_FILE)

        with DofusDbClient() as client:
            quests = client.fetch_quests()

        self.cache.save(
            self.CACHE_FILE,
            quests,
        )

        return quests