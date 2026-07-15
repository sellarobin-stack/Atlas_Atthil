from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class AtlasExporter:
    """
    Exporte les données normalisées au format Atlas.
    """

    def __init__(
        self,
        output_directory: Path,
    ) -> None:

        self.output_directory = output_directory

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def export(
        self,
        filename: str,
        data: list[dict[str, Any]],
    ) -> Path:

        destination = self.output_directory / filename

        with destination.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4,
            )

        return destination