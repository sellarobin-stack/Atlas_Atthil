from __future__ import annotations

from app.data_pipeline.models import AtlasStep
from app.data_pipeline.normalizers.objective_normalizer import (
    ObjectiveNormalizer,
)
from app.data_pipeline.normalizers.reward_normalizer import (
    RewardNormalizer,
)


class StepNormalizer:

    @staticmethod
    def normalize(data: dict) -> AtlasStep:

        step = AtlasStep(
            id=data["id"],
            name=data.get("name", ""),
            order=data.get("order", 0),
            optional=data.get("optional", False),
        )

        for objective in data.get("objectives", []):
            step.add_objective(
                ObjectiveNormalizer.normalize(objective)
            )

        for reward in data.get("rewards", []):
            step.add_reward(
                RewardNormalizer.normalize(reward)
            )

        return step