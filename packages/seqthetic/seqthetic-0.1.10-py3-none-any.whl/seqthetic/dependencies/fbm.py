from typing import List

from tqdm import tqdm
from pydantic import Field
from stochastic.processes.continuous import FractionalBrownianMotion

from seqthetic.dependencies.base import BaseDependency, DependencyResult, SchemaList
from seqthetic.range import FlexibleRange
from seqthetic.utils import make_digitizer, sample_integer_range
from joblib import Parallel, delayed, parallel_backend


class FBMDependency(BaseDependency):
    """
    Dependency from discretized fractional brownian motion(fBm).

    Attributes:
        hurst: Hurst exponent for the fbm
        discretize_ratio: ratio for discretizing: binning into round(length * binning_ratio) bins. range (0, 1]
        sequence_vocab_size: size of the vocabulary for each sequence
    """

    generator: str = "fbm"

    hurst: FlexibleRange = Field(...)
    discretize_ratio: FlexibleRange = Field(...)
    metadata_schema: List[str] = SchemaList(["hurst", "discretize_ratio"])

    custom_seed_schema: List[str] = SchemaList(
        ["hurst", "discretize_ratio", "dependency"]
    )

    def report_param(self):
        return f"Hurst: {self.hurst}, Discretize_ratio: {self.discretize_ratio}"

    def prepare_params(self, num_sequence: int):
        rngs = {}
        for field in ["hurst", "sequence_length", "discretize_ratio", "dependency"]:
            rngs[field] = self.seed.get_rng(field)

        dep_rngs = self.seed.get_rng("dependency", num_sequence, return_list=True)

        # sample parameters
        hursts = rngs["hurst"].uniform(self.hurst.min, self.hurst.max, num_sequence)
        
        lengths = sample_integer_range(self.sequence_length, rngs["sequence_length"], num_sequence)
        
        discretize_ratio = rngs["discretize_ratio"].uniform(
            self.discretize_ratio.min, self.discretize_ratio.max, num_sequence
        )
        # return a list and create
        metadata = [
            {"hurst": h, "sequence_length": l, "discretize_ratio": b}
            for h, l, b in tqdm(
                zip(hursts, lengths, discretize_ratio), desc="fbm, metadata"
            )
        ]
        return [
            param
            for param in tqdm(
                zip(
                    lengths,
                    hursts,
                    discretize_ratio,
                    dep_rngs,
                ),
                desc="making Dependency params",
            )
        ], metadata

    @staticmethod
    def make_dependency(params):
        length, hurst, discretize_ratio, dep_rng = params
        fbm = FractionalBrownianMotion(hurst, rng=dep_rng)
        deps_raw = fbm.sample(length - 1)
        digitize = make_digitizer(discretize_ratio)
        deps = digitize(deps_raw)
        return deps
