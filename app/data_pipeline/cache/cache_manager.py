from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class CacheManager:

    def __init__(self, cache_directory: str | Path):

        self.cache_directory = Path(cache_directory)

        self.cache_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def exists(self, filename: str) -> bool:

        return (self.cache_directory / filename).exists()

    def load(self, filename: str) -> Any:

        with (self.cache_directory / filename).open(
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)

    def save(
        self,
        filename: str,
        data: Any,
    ) -> Path:

        path = self.cache_directory / filename

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

        return path

    def delete(self, filename: str) -> None:

        path = self.cache_directory / filename

        if path.exists():
            path.unlink()

    def clear(self) -> None:

        for file in self.cache_directory.glob("*.json"):
            file.unlink()