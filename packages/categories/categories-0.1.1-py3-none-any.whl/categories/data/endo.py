from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.type import Lambda, forall

__all__ = (
    'Endo',
)


a = TypeVar('a')


@dataclass(frozen=True)
class Endo(forall[a]):
    apply : Lambda[a, a]
