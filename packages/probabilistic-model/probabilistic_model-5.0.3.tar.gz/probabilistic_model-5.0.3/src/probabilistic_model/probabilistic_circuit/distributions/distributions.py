from __future__ import annotations

from abc import ABC

import numpy as np
from random_events.interval import SimpleInterval, Interval
from random_events.product_algebra import Event, SimpleEvent
from random_events.variable import Variable
from sortedcontainers import SortedSet
from typing_extensions import Tuple, Optional, Self

from ...distributions.distributions import (ContinuousDistribution as PMContinuousDistribution,
                                            DiracDeltaDistribution as PMDiracDeltaDistribution,
                                            SymbolicDistribution as PMSymbolicDistribution,
                                            IntegerDistribution as PMIntegerDistribution,
                                            DiscreteDistribution as PMDiscreteDistribution,
                                            UnivariateDistribution as PMUnivariateDistribution)
from ..probabilistic_circuit import (DeterministicSumUnit, ProbabilisticCircuitMixin, cache_inference_result,
                                     SmoothSumUnit)
from ...distributions.uniform import UniformDistribution as PMUniformDistribution
from ...distributions.gaussian import (GaussianDistribution as PMGaussianDistribution,
                                       TruncatedGaussianDistribution as PMTruncatedGaussianDistribution)
from ...utils import MissingDict


class UnivariateDistribution(PMUnivariateDistribution, ProbabilisticCircuitMixin, ABC):

    def is_deterministic(self) -> bool:
        return True

    @property
    def variables(self) -> SortedSet:
        return SortedSet([self.variable])

    def __hash__(self):
        return ProbabilisticCircuitMixin.__hash__(self)

    @cache_inference_result
    def log_conditional_of_simple_event(self, event: SimpleEvent) -> Tuple[Optional[Self], float]:
        return super().log_conditional(event.as_composite_set())

    @cache_inference_result
    def simplify(self) -> Self:
        return self.__copy__()

    def empty_copy(self) -> Self:
        return self.__copy__()


class ContinuousDistribution(UnivariateDistribution, PMContinuousDistribution, ProbabilisticCircuitMixin, ABC):

    def log_conditional_from_interval(self, interval: Interval) -> Tuple[DeterministicSumUnit, float]:
        result = DeterministicSumUnit()
        total_probability = 0.

        for simple_interval in interval.simple_sets:
            current_conditional, current_log_probability = self.log_conditional_from_simple_interval(simple_interval)
            current_probability = np.exp(current_log_probability)
            result.add_subcircuit(current_conditional, current_probability)
            total_probability += current_probability

        result.normalize()

        return result, np.log(total_probability)

    def log_conditional_from_singleton(self, interval: SimpleInterval) -> Tuple[DiracDeltaDistribution, float]:
        conditional, probability = super().log_conditional_from_singleton(interval)
        return DiracDeltaDistribution(conditional.variable, conditional.location,
                                      conditional.density_cap), probability


class DiscreteDistribution(UnivariateDistribution, PMDiscreteDistribution, ProbabilisticCircuitMixin, ABC):

    def as_deterministic_sum(self) -> DeterministicSumUnit:
        """
        Convert this distribution to a deterministic sum unit that encodes the same distribution.
        The result has as many children as the domain of the variable and each child encodes the value of the variable.

        :return: A deterministic sum unit that encodes the same distribution.
        """
        result = DeterministicSumUnit()

        for event in self.variable.domain.simple_sets:
            event = SimpleEvent({self.variable: event}).as_composite_set()
            conditional, probability = self.conditional(event)
            result.add_subcircuit(conditional, probability)

        return result

    @classmethod
    def from_sum_unit(cls, sum_unit: SmoothSumUnit):
        """
        Create a discrete distribution from a sum unit.

        :param sum_unit: The sum unit to create the distribution from.
        :return: The discrete distribution.
        """
        assert len(sum_unit.variables) == 1, "Can only convert unidimensional sum units to discrete distributions."
        variable = sum_unit.variables[0]
        probabilities = MissingDict(float)

        for element in sum_unit.support().simple_sets[0][variable].simple_sets:
            probability = sum_unit.probability_of_simple_event(SimpleEvent({variable: element}))
            if isinstance(element, SimpleInterval):
                element = element.lower
            probabilities[int(element)] = probability
        return cls(variable, probabilities)


class DiracDeltaDistribution(ContinuousDistribution, PMDiracDeltaDistribution):
    ...


class UniformDistribution(ContinuousDistribution, PMUniformDistribution):
    ...


class GaussianDistribution(ContinuousDistribution, PMGaussianDistribution):

    def log_conditional_from_non_singleton_simple_interval(self, interval: SimpleInterval) -> (
            Tuple)[TruncatedGaussianDistribution, float]:
        conditional, log_probability = (PMGaussianDistribution.
                                        log_conditional_from_non_singleton_simple_interval(self, interval))
        return TruncatedGaussianDistribution(conditional.variable, conditional.interval,
                                             conditional.location, conditional.scale), log_probability


class TruncatedGaussianDistribution(GaussianDistribution, ContinuousDistribution, PMTruncatedGaussianDistribution):
    ...


class IntegerDistribution(DiscreteDistribution, PMIntegerDistribution):
    ...


class SymbolicDistribution(DiscreteDistribution, PMSymbolicDistribution):
    ...
