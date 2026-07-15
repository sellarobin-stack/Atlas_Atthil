from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from app.data_pipeline.models import AtlasQuest


class JsonExporter:

    @staticmethod
    def export(
        quests: list[AtlasQuest],
        output: str | Path,
    ) -> None:

        output = Path(output)

        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                [asdict(q) for q in quests],
                file,
                indent=4,
                ensure_ascii=False,
            )