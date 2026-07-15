from __future__ import annotations

from typing import Any

import requests


class DofusDbSource:
    """
    Client DofusDB.

    Cette classe est la seule autorisée à connaître
    l'API DofusDB.
    """

    BASE_URL = "https://api.dofusdb.fr"

    def __init__(
        self,
        timeout: int = 30,
    ) -> None:

        self.timeout = timeout

    def _get(
        self,
        endpoint: str,
    ) -> Any:

        response = requests.get(
            f"{self.BASE_URL}{endpoint}",
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response.json()

    # ------------------------------------------------------------------
    # Quests
    # ------------------------------------------------------------------

    def get_quest(
        self,
        quest_id: int,
    ) -> dict[str, Any]:

        return self._get(
            f"/quests/{quest_id}"
        )

    def get_quests(self) -> list[dict[str, Any]]:

        return self._get(
            "/quests"
        )

    # ------------------------------------------------------------------
    # NPCs
    # ------------------------------------------------------------------

    def get_npc(
        self,
        npc_id: int,
    ) -> dict[str, Any]:

        return self._get(
            f"/npcs/{npc_id}"
        )

    def get_npcs(self) -> list[dict[str, Any]]:

        return self._get(
            "/npcs"
        )

    # ------------------------------------------------------------------
    # Maps
    # ------------------------------------------------------------------

    def get_map(
        self,
        map_id: int,
    ) -> dict[str, Any]:

        return self._get(
            f"/maps/{map_id}"
        )

    def get_maps(self) -> list[dict[str, Any]]:

        return self._get(
            "/maps"
        )

    # ------------------------------------------------------------------
    # Items
    # ------------------------------------------------------------------

    def get_item(
        self,
        item_id: int,
    ) -> dict[str, Any]:

        return self._get(
            f"/items/{item_id}"
        )

    def get_items(self) -> list[dict[str, Any]]:

        return self._get(
            "/items"
        )