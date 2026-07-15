from __future__ import annotations

import json
from pathlib import Path


class CacheManager:

    def __init__(self, cache_directory: str | Path):

        self.cache_directory = Path(cache_directory)

        self.cache_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def has(self, filename: str) -> bool:
        return (self.cache_directory / filename).exists()

    def load(self, filename: str):

        with (self.cache_directory / filename).open(
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def save(
        self,
        filename: str,
        data,
    ) -> None:

        with (self.cache_directory / filename).open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )