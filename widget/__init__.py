"""
WIT interface for the interaction between the host application and widgets
Inspired by work-in-progress WASI Preview 2 WIT definitions
(https://github.com/bytecodealliance/preview2-prototyping/tree/main/wit)
"""
from typing import TypeVar, Generic, Union, Optional, Protocol, Tuple, List, Any, Self
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from .types import Result, Ok, Err, Some
from .imports import types


class Widget(Protocol):

    @abstractmethod
    def get_name(self) -> str:
        """
        Return the name of the widget
        """
        raise NotImplementedError

    @abstractmethod
    def get_version(self) -> str:
        """
        Return the semantic version of the widget
        """
        raise NotImplementedError

    @abstractmethod
    def get_config_schema(self) -> str:
        """
        Return the config JSON schema string
        """
        raise NotImplementedError

    @abstractmethod
    def get_run_update_cycle_seconds(self) -> int:
        """
        Returns the run update cycle in seconds.
        With this, widgets can control how frequently they shall be updated.
        """
        raise NotImplementedError

    @abstractmethod
    def run(self, context: types.WidgetContext) -> types.WidgetResult:
        """
        Invoke the widget with the given context
        """
        raise NotImplementedError

