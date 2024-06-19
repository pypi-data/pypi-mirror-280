from __future__ import annotations

from dataclasses import dataclass
from itertools import count
from typing import TypeVar

from categories.type import Stream, typeclass

__all__ = (
    'Bounded',
    'Enum',
    'boundedEnumFrom',
    'boundedEnumFromThen',
)


a = TypeVar('a')


@dataclass(frozen=True)
class Bounded(typeclass[a]):
    def min(self, /) -> a: ...

    def max(self, /) -> a: ...


@dataclass(frozen=True)
class Enum(typeclass[a]):
    def succ(self, x : a, /) -> a:
        return self.inject(self.project(x) + 1)

    def pred(self, x : a, /) -> a:
        return self.inject(self.project(x) - 1)

    def inject(self, x : int, /) -> a: ...

    def project(self, x : a, /) -> int: ...

    def enumFrom(self, x : a, /) -> Stream[a]:
        return map(self.inject, count(self.project(x)))

    def enumFromThen(self, x : a, y : a, /) -> Stream[a]:
        return map(self.inject, count(self.project(x), self.project(y) - self.project(x)))

    def enumFromTo(self, x : a, y : a, /) -> Stream[a]:
        return map(self.inject, range(self.project(x), self.project(y) + 1))

    def enumFromThenTo(self, x : a, y : a, z : a, /) -> Stream[a]:
        return map(self.inject, range(self.project(x), self.project(z) + 1, self.project(y) - self.project(x)))


def boundedEnumFrom(enum : Enum[a], bounded : Bounded[a], x : a, /) -> Stream[a]:
    return map(enum.inject, range(enum.project(x), enum.project(bounded.max()) + 1))


def boundedEnumFromThen(enum : Enum[a], bounded : Bounded[a], x : a, y : a, /) -> Stream[a]:
    match (enum.project(x), enum.project(y)):
        case x_, y_ if (y_ >= x_):
            return map(enum.inject, range(x_, enum.project(bounded.max()) + 1, y_ - x_))
        case x_, y_:
            return map(enum.inject, range(x_, enum.project(bounded.min()) - 1, y_ - x_))
