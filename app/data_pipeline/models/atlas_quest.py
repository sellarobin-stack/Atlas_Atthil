from __future__ import annotations

from dataclasses import dataclass, field

from .atlas_map import AtlasMap
from .atlas_npc import AtlasNpc
from .atlas_prerequisite import AtlasPrerequisite
from .atlas_reward import AtlasReward
from .atlas_step import AtlasStep


@dataclass(slots=True)
class AtlasQuest:
    id: int

    name: str

    level: int | None = None

    category: str | None = None

    campaign: str | None = None

    repeatable: bool = False

    start_npcs: list[AtlasNpc] = field(default_factory=list)

    start_maps: list[AtlasMap] = field(default_factory=list)

    prerequisites: list[AtlasPrerequisite] = field(default_factory=list)

    steps: list[AtlasStep] = field(default_factory=list)

    final_rewards: list[AtlasReward] = field(default_factory=list)

    def add_step(self, step: AtlasStep) -> None:
        self.steps.append(step)

    def add_start_npc(self, npc: AtlasNpc) -> None:
        self.start_npcs.append(npc)

    def add_start_map(self, game_map: AtlasMap) -> None:
        self.start_maps.append(game_map)

    def add_prerequisite(self, prerequisite: AtlasPrerequisite) -> None:
        self.prerequisites.append(prerequisite)

    def add_reward(self, reward: AtlasReward) -> None:
        self.final_rewards.append(reward)

    @property
    def step_count(self) -> int:
        return len(self.steps)

    @property
    def objective_count(self) -> int:
        return sum(len(step.objectives) for step in self.steps)

    @property
    def reward_count(self) -> int:
        return (
            len(self.final_rewards)
            + sum(len(step.rewards) for step in self.steps)
        )