from __future__ import annotations

from typing import Any

import requests


class DofusDbClient:

    BASE_URL = "https://api.dofusdb.fr"

    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.session = requests.Session()

    def fetch_quests(self) -> list[dict[str, Any]]:
        response = self.session.get(
            f"{self.BASE_URL}/quests",
            timeout=self.timeout,
        )

        response.raise_for_status()

        data = response.json()

        if isinstance(data, list):
            return data

        if isinstance(data, dict):
            if "data" in data:
                return data["data"]

            if "quests" in data:
                return data["quests"]

        raise RuntimeError("Unexpected DofusDB response.")

    def fetch_quest(self, quest_id: int) -> dict[str, Any]:
        response = self.session.get(
            f"{self.BASE_URL}/quests/{quest_id}",
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response.json()

    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> "DofusDbClient":
        return self

    def __exit__(self, *_):
        self.close()