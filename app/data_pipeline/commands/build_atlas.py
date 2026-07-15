from __future__ import annotations

from pathlib import Path

from app.data_pipeline.builder import AtlasPipeline
from app.data_pipeline.cache.cache_manager import CacheManager
from app.data_pipeline.services import QuestDownloader


ROOT_DIR = Path(__file__).resolve().parents[3]

CACHE_DIRECTORY = (
    ROOT_DIR
    / "app"
    / "data_pipeline"
    / "cache"
)

OUTPUT_DIRECTORY = (
    ROOT_DIR
    / "app"
    / "data_pipeline"
    / "output"
)


def main() -> None:

    print("=" * 60)
    print("ATLAS DATA PIPELINE")
    print("=" * 60)
    print()

    cache = CacheManager(CACHE_DIRECTORY)

    downloader = QuestDownloader(cache)

    print("Downloading quests...")

    raw_quests = downloader.download()

    print(f"{len(raw_quests)} quests loaded.")

    pipeline = AtlasPipeline(
        output_directory=OUTPUT_DIRECTORY,
    )

    output_file, statistics = pipeline.run(
        raw_quests,
    )

    print()
    print(statistics)
    print()
    print(f"Atlas dataset exported to:")
    print(output_file)
    print()


if __name__ == "__main__":
    main()