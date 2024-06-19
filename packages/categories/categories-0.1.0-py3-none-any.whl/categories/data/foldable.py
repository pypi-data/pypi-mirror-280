from __future__ import annotations

from dataclasses import dataclass
from functools import partial
from typing import TypeVar

from categories.control.monad import Monad
from categories.data.dual import Dual
from categories.data.endo import Endo
from categories.data.maybe import Just, Maybe, Nothing
from categories.data.monoid import Monoid, MonoidDual, MonoidEndo
from categories.type import Expr, Lambda, hkt, typeclass

__all__ = (
    'Foldable',
    'foldrM',
    'foldlM',
)


a = TypeVar('a')

b = TypeVar('b')

m = TypeVar('m')

t = TypeVar('t')


@dataclass(frozen=True)
class Foldable(typeclass[t]):
    def fold(self, inst : Monoid[m], xs : hkt[t, m], /) -> m:
        return self.foldMap(inst, lambda x, /: x, xs)

    def foldMap(self, inst : Monoid[m], f : Lambda[a, m], xs : hkt[t, a], /) -> m:
        def g(x : a, y : m, /) -> m:
            return inst.append(f(x), y)
        return self.foldr(g, inst.unit(), xs)

    def foldMap_(self, inst : Monoid[m], f : Lambda[a, m], xs : hkt[t, a], /) -> m:
        def g(x : m, y : a, /) -> m:
            return inst.append(x, f(y))
        return self.foldl_(g, inst.unit(), xs)

    def foldr(self, f : Expr[[a, b], b], z : b, xs : hkt[t, a], /) -> b:
        def g(x : a, /) -> Endo[b]:
            return Endo(partial(f, x))
        return self.foldMap(MonoidEndo(), g, xs).apply(z)

    def foldr_(self, f : Expr[[a, b], b], z : b, xs : hkt[t, a], /) -> b:
        def g(k : Lambda[b, b], x : a, /) -> Lambda[b, b]:
            return lambda y, /: k(f(x, y))
        return self.foldl(g, lambda x, /: x, xs)(z)

    def foldl(self, f : Expr[[b, a], b], z : b, xs : hkt[t, a], /) -> b:
        def g(x : a, /) -> Dual[Endo[b]]:
            return Dual(Endo(lambda y, /: f(y, x)))
        return self.foldMap(MonoidDual(MonoidEndo()), g, xs).project.apply(z)

    def foldl_(self, f : Expr[[b, a], b], z : b, xs : hkt[t, a], /) -> b:
        def g(x : a, k : Lambda[b, b], /) -> Lambda[b, b]:
            return lambda y, /: k(f(y, x))
        return self.foldr(g, lambda x, /: x, xs)(z)

    def foldr1(self, f : Expr[[a, a], a], xs : hkt[t, a], /) -> a:
        def g(x : a, m : Maybe[a], /) -> Maybe[a]:
            match m:
                case Nothing():
                    return Just(x)
                case Just(y):
                    return Just(f(x, y))

        match self.foldr(g, Nothing(), xs):
            case Nothing():
                assert None
            case Just(x):
                return x

    def foldl1(self, f : Expr[[a, a], a], xs : hkt[t, a], /) -> a:
        def g(m : Maybe[a], y : a, /) -> Maybe[a]:
            match m:
                case Nothing():
                    return Just(y)
                case Just(x):
                    return Just(f(x, y))

        match self.foldl(g, Nothing(), xs):
            case Nothing():
                assert None
            case Just(x):
                return x


def foldrM(foldable : Foldable[t], monad : Monad[m],
           f : Expr[[a, b], hkt[m, b]], z : b, xs : hkt[t, a], /) -> hkt[m, b]:
    def g(k : Lambda[b, hkt[m, b]], x : a, /) -> Lambda[b, hkt[m, b]]:
        return lambda y, /: monad.bind(f(x, y), k)
    return foldable.foldl(g, monad.inject, xs)(z)


def foldlM(foldable : Foldable[t], monad : Monad[m],
           f : Expr[[b, a], hkt[m, b]], z : b, xs : hkt[t, a], /) -> hkt[m, b]:
    def g(x : a, k : Lambda[b, hkt[m, b]], /) -> Lambda[b, hkt[m, b]]:
        return lambda y, /: monad.bind(f(y, x), k)
    return foldable.foldr(g, monad.inject, xs)(z)
