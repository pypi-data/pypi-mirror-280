from __future__ import annotations

from abc import abstractmethod
from collections import defaultdict

import numpy as np
from random_events.interval import SimpleInterval, Interval
from random_events.variable import Continuous
from typing_extensions import Dict, Any, Self, TYPE_CHECKING, Type, Tuple, List
from random_events.utils import get_full_class_name, recursive_subclasses
import types
from .constants import *


def simple_interval_as_array(interval: SimpleInterval) -> np.ndarray:
    """
    Convert a simple interval to a numpy array.
    :param interval:  The interval
    :return:  [lower, upper] as numpy array
    """
    return np.array([interval.lower, interval.upper])


def interval_as_array(interval: Interval) -> np.ndarray:
    """
    Convert an interval to a numpy array.
    The resulting array has shape (n, 2) where n is the number of simple intervals in the interval.
    The first column contains the lower bounds and the second column the upper bounds of the simple intervals.
    :param interval: The interval
    :return:  as numpy array
    """
    return np.array([simple_interval_as_array(simple_interval) for simple_interval in interval.simple_sets])


def type_converter(abstract_type: Type, package: types.ModuleType):
    """
    Convert a type to a different type from a target sub-package that inherits from this type.

    :param abstract_type: The type to convert
    :param package: The sub-package to search in for that type

    :return: The converted type
    """
    for subclass in recursive_subclasses(abstract_type):
        if subclass.__module__.startswith(package.__name__):
            return subclass

    raise ValueError("Could not find type {} in package {}".format(abstract_type, package))


class SubclassJSONSerializer:
    """
    Class for automatic (de)serialization of subclasses.
    Classes that inherit from this class can be serialized and deserialized automatically by calling this classes
    'from_json' method.
    """

    def to_json(self) -> Dict[str, Any]:
        return {"type": get_full_class_name(self.__class__)}

    @classmethod
    def _from_json(cls, data: Dict[str, Any]) -> Self:
        """
        Create a variable from a json dict.
        This method is called from the from_json method after the correct subclass is determined and should be
        overwritten by the respective subclass.

        :param data: The json dict
        :return: The deserialized object
        """
        raise NotImplementedError()

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> Self:
        """
        Create the correct instanceof the subclass from a json dict.

        :param data: The json dict
        :return: The correct instance of the subclass
        """
        for subclass in recursive_subclasses(SubclassJSONSerializer):
            if get_full_class_name(subclass) == data["type"]:
                return subclass._from_json(data)

        raise ValueError("Unknown type {}".format(data["type"]))


class MissingDict(defaultdict):
    """
    A defaultdict that returns the default value when the key is missing and does **not** add the key to the dict.
    """
    def __missing__(self, key):
        return self.default_factory()
