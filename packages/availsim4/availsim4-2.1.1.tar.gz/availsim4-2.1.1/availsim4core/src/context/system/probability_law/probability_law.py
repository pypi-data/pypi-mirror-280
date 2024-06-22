# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved.

from typing import List, Optional
import numpy


class ProbabilityLaw:
    """
    Distributive Function which is used to evaluate the failure and repair times.
    """
    __slots__ = 'name', 'parameters', 'is_failure_on_demand'
    random_number_generator = numpy.random.default_rng()

    def __init__(self,
                 name: str,
                 parameters: List[float],
                 is_failure_on_demand: bool):
        self.name = name
        self.parameters = parameters
        self.is_failure_on_demand = is_failure_on_demand

    def __str__(self):
        return f"{self.name} -> {self.parameters}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name and \
               self.parameters == other.parameters

    @classmethod
    def set_seed(cls, seed: Optional[int]):
        """Function seeds seed for a generator used by all probability funcitons which inherit from this class.

        Args: 
            seed:
                An integer which will be used as a seed for the numpy's random number generator. If None, then 
                understood as a request for a "random" seed -- in other words, "fresh, unpredictable entropy will be
                pulled from the OS" as stated in [1].

        [1] https://numpy.org/doc/stable/reference/random/generator.html
        """
        cls.random_number_generator = numpy.random.default_rng(seed)

    def get_random_value(self) -> float:
        pass

    def get_quantile_value(self, quantile: float) -> float:
        pass

    def get_mean_value(self) -> float:
        pass

    def get_variance_value(self) -> float:
        pass
