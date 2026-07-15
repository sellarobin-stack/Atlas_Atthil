from __future__ import annotations

from pathlib import Path

from app.data_pipeline.exporters import JsonExporter
from app.data_pipeline.models import AtlasQuest


class AtlasBuilder:

    def __init__(self, output_directory: str | Path):

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def build(
        self,
        quests: list[AtlasQuest],
    ) -> Path:

        output_file = self.output_directory / "atlas_data.json"

        JsonExporter.export(
            quests,
            output_file,
        )

        return output_file