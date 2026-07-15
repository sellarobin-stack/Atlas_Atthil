from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class BuildStatistics:

    quests_downloaded: int = 0

    quests_normalized: int = 0

    quests_exported: int = 0

    build_duration: float = 0.0

    def __str__(self) -> str:

        return (
            "\n"
            "========== BUILD SUMMARY ==========\n"
            f"Downloaded : {self.quests_downloaded}\n"
            f"Normalized : {self.quests_normalized}\n"
            f"Exported   : {self.quests_exported}\n"
            f"Duration   : {self.build_duration:.2f}s\n"
            "===================================\n"
        )