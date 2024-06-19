from __future__ import annotations

from typing import TypeVar

from categories.type import Expr, Map, Thunk, Void

__all__ = (
    'force',
    'let',
    'rec',
    'seq',
    'undefined',
)


a = TypeVar('a')

b = TypeVar('b')


def force(x : Thunk[a], /) -> a: return x()


def let(**_ : a) -> Map[str, a]: return Map(_)


def rec(*fs : Expr[..., a]) -> tuple[Expr[..., a], ...]:
    return (x := (*map(lambda f, /: lambda *_: f(*x, *_), fs),))


def seq(_ : a, x : b, /) -> b: return x


def undefined() -> Void: assert None, '⊥'
