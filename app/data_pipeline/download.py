from __future__ import annotations

import json
from pathlib import Path

import requests


class Downloader:
    """
    Télécharge des ressources JSON et les enregistre
    dans le dossier data/raw.
    """

    def __init__(
        self,
        output_directory: Path,
        timeout: int = 30,
    ) -> None:

        self.output_directory = output_directory
        self.timeout = timeout

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def download(
        self,
        url: str,
        filename: str,
    ) -> Path:

        response = requests.get(
            url,
            timeout=self.timeout,
        )

        response.raise_for_status()

        destination = self.output_directory / filename

        with destination.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                response.json(),
                file,
                ensure_ascii=False,
                indent=4,
            )

        return destination