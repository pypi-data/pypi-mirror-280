from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.data.functor import Functor, FunctorIO, FunctorLambda, FunctorList, FunctorParser
from categories.text.parser import Parser
from categories.type import IO, Lambda, _, hkt, typeclass

__all__ = (
    'Applicative',
    'ApplicativeIO',
    'ApplicativeLambda',
    'ApplicativeList',
    'ApplicativeParser',
)


a = TypeVar('a')

b = TypeVar('b')

f = TypeVar('f')

r = TypeVar('r')


@dataclass(frozen=True)
class Applicative(Functor[f], typeclass[f]):
    def inject(self, x : a, /) -> hkt[f, a]: ...

    def apply(self, f : hkt[f, Lambda[a, b]], x : hkt[f, a], /) -> hkt[f, b]: ...

    def seq(self, _ : hkt[f, a], x : hkt[f, b], /) -> hkt[f, b]:
        return self.apply(self.const(lambda x, /: x, _), x)


@dataclass(frozen=True)
class ApplicativeIO(FunctorIO, Applicative[IO]):
    async def inject(self, x : a, /) -> a:
        return x

    async def apply(self, m : IO[Lambda[a, b]], m_ : IO[a], /) -> b:
        match (await m, await m_):
            case f, x:
                return f(x)


@dataclass(frozen=True)
class ApplicativeLambda(FunctorLambda[r], Applicative[Lambda[r, _]]):
    def inject(self, x : a, /) -> Lambda[r, a]:
        return lambda _, /: x

    def apply(self, f : Lambda[r, Lambda[a, b]], g : Lambda[r, a], /) -> Lambda[r, b]:
        return lambda x, /: f(x)(g(x))


@dataclass(frozen=True)
class ApplicativeList(FunctorList, Applicative[list]):
    def inject(self, x : a, /) -> list[a]:
        return [x]

    def apply(self, fs : list[Lambda[a, b]], xs : list[a], /) -> list[b]:
        return [f(x) for f in fs for x in xs]


@dataclass(frozen=True)
class ApplicativeParser(FunctorParser, Applicative[Parser]):
    def inject(self, x : a, /) -> Parser[a]:
        return lambda s, /: [(x, s)]

    def apply(self, p : Parser[Lambda[a, b]], q : Parser[a], /) -> Parser[b]:
        return lambda s, /: [(f(x), s) for (f, s) in p(s) for (x, s) in q(s)]
