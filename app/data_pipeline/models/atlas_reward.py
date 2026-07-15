from dataclasses import dataclass


@dataclass(slots=True)
class AtlasReward:
    """
    Représentation interne d'une récompense de quête.
    """

    experience: int = 0

    kamas: int = 0

    items: list[tuple[int, int]] | None = None

    emotes: list[int] | None = None

    titles: list[int] | None = None

    ornaments: list[int] | None = None

    achievements: list[int] | None = None

    spells: list[int] | None = None

    jobs: list[int] | None = None

    def __post_init__(self) -> None:

        if self.items is None:
            self.items = []

        if self.emotes is None:
            self.emotes = []

        if self.titles is None:
            self.titles = []

        if self.ornaments is None:
            self.ornaments = []

        if self.achievements is None:
            self.achievements = []

        if self.spells is None:
            self.spells = []

        if self.jobs is None:
            self.jobs = []