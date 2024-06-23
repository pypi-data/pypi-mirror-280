from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.data.identity import Identity
from categories.data.maybe import Maybe, Nothing, Just
from categories.text.parser import Parser
from categories.type import IO, Lambda, _, hkt, typeclass

__all__ = (
    'Functor',
    'FunctorIO',
    'FunctorIdentity',
    'FunctorLambda',
    'FunctorList',
    'FunctorMaybe',
    'FunctorParser',
)


a = TypeVar('a')

b = TypeVar('b')

f = TypeVar('f')

r = TypeVar('r')


@dataclass(frozen=True)
class Functor(typeclass[f]):
    def map(self, f : Lambda[a, b], x : hkt[f, a], /) -> hkt[f, b]: ...

    def const(self, x : a, _ : hkt[f, b], /) -> hkt[f, a]:
        return self.map(lambda _, /: x, _)


@dataclass(frozen=True)
class FunctorIO(Functor[IO]):
    async def map(self, f : Lambda[a, b], m : IO[a], /) -> b:
        match await m:
            case x:
                return f(x)


@dataclass(frozen=True)
class FunctorIdentity(Functor[Identity]):
    def map(self, f : Lambda[a, b], x : Identity[a], /) -> Identity[b]:
        match x:
            case Identity(x):
                return Identity(f(x))


@dataclass(frozen=True)
class FunctorLambda(Functor[Lambda[r, _]]):
    def map(self, f : Lambda[a, b], g : Lambda[r, a], /) -> Lambda[r, b]:
        return lambda x, /: f(g(x))


@dataclass(frozen=True)
class FunctorList(Functor[list]):
    def map(self, f : Lambda[a, b], xs : list[a], /) -> list[b]:
        return [f(x) for x in xs]


@dataclass(frozen=True)
class FunctorMaybe(Functor[Maybe]):
    def map(self, f : Lambda[a, b], m : Maybe[a], /) -> Maybe[b]:
        match m:
            case Nothing():
                return Nothing()
            case Just(x):
                return Just(f(x))


@dataclass(frozen=True)
class FunctorParser(Functor[Parser]):
    def map(self, f : Lambda[a, b], p : Parser[a], /) -> Parser[b]:
        return lambda s, /: [(f(x), s) for (x, s) in p(s)]
