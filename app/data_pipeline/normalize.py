from __future__ import annotations

from pathlib import Path

from app.data_pipeline.exporters.atlas_exporter import AtlasExporter
from app.data_pipeline.normalizers.quest_normalizer import QuestNormalizer


class Normalizer:

    def __init__(
        self,
        output_directory: Path,
    ) -> None:

        self.exporter = AtlasExporter(
            output_directory,
        )

    def normalize_quests(
        self,
        quests: list[dict],
    ) -> None:

        atlas_quests = []

        for quest in quests:

            atlas = QuestNormalizer.normalize(
                quest,
            )

            atlas_quests.append(
                atlas.__dict__
            )

        self.exporter.export(
            "quests.json",
            atlas_quests,
        )