from __future__ import annotations

from dataclasses import dataclass, field

from .atlas_objective import AtlasObjective
from .atlas_reward import AtlasReward


@dataclass(slots=True)
class AtlasStep:
    id: int

    name: str

    order: int

    objectives: list[AtlasObjective] = field(default_factory=list)

    rewards: list[AtlasReward] = field(default_factory=list)

    optional: bool = False

    completed: bool = False

    def add_objective(self, objective: AtlasObjective) -> None:
        self.objectives.append(objective)

    def add_reward(self, reward: AtlasReward) -> None:
        self.rewards.append(reward)