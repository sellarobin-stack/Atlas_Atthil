from __future__ import annotations

from pathlib import Path

from app.data_pipeline.builder.atlas_builder import AtlasBuilder
from app.data_pipeline.builder.statistics import BuildStatistics
from app.data_pipeline.parsers import DofusDbQuestParser


class AtlasPipeline:

    def __init__(
        self,
        output_directory: str | Path,
    ):

        self.builder = AtlasBuilder(output_directory)

    def run(
        self,
        raw_quests: list[dict],
    ) -> tuple[Path, BuildStatistics]:

        statistics = BuildStatistics()

        statistics.quests_downloaded = len(raw_quests)

        atlas_quests = []

        for quest in raw_quests:
            atlas_quests.append(
                DofusDbQuestParser.parse(quest)
            )

        statistics.quests_normalized = len(atlas_quests)

        output = self.builder.build(
            atlas_quests
        )

        statistics.quests_exported = len(atlas_quests)

        return output, statistics