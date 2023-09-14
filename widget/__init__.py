from typing import TypeVar, Generic, Union, Optional, Union, Protocol, Tuple, List
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod

from .types import Result, Ok, Err, Some
import componentize_py_runtime
from .imports import types


class Widget(Protocol):

    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_version(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_config_schema(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_run_update_cycle_seconds(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def run(self, context: types.WidgetContext) -> types.WidgetResult:
        raise NotImplementedError

