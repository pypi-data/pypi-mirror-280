from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.type import forall

__all__ = (
    'Identity',
)


a = TypeVar('a')


@dataclass(frozen=True)
class Identity(forall[a]):
    project : a
