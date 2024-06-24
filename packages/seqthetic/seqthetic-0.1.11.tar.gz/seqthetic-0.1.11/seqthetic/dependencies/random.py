from typing import List

import numpy as np

from seqthetic.dependencies.base import BaseDependency, DependencyResult, SchemaList
from seqthetic.range import FlexibleRange
from seqthetic.utils import sample_integer_range


class RandomDependency(BaseDependency):
    """Dependency from random number generator"""

    generator: str = "random"
    num_dependency: FlexibleRange
    metadata_schema: List[str] = SchemaList(["num_dependency"])
    custom_seed_schema: List[str] = SchemaList(["num_dependency"])

    def prepare_params(self, num_sequence: int) -> tuple[list[tuple], list[dict]]:
        dep_rng = self.seed.get_rng("num_dependency")
        length_rng = self.seed.get_rng("sequence_length")
        num_dependencies = sample_integer_range(self.num_dependency, dep_rng, num_sequence)

        sequence_lengths = sample_integer_range(
            self.sequence_length, length_rng, num_sequence
        )
        metadata = [
            {"num_dependency": n, "sequence_length": l}
            for n, l in zip(num_dependencies, sequence_lengths)
        ]
        return [
            params for params in zip(dep_rng, num_dependencies, sequence_lengths)
        ], metadata

    @staticmethod
    def make_dependency(params: tuple[np.random.Generator, int, int]):
        dep_rng, num_dependencies, sequence_length = params
        dependency = dep_rng.integers(num_dependencies, size=sequence_length)

        return dependency
