from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.control.applicative import Applicative, ApplicativeIO, ApplicativeIdentity, ApplicativeLambda, ApplicativeList, ApplicativeMaybe, ApplicativeParser
from categories.data.identity import Identity
from categories.data.maybe import Maybe, Nothing, Just
from categories.text.parser import Parser
from categories.type import IO, Lambda, _, hkt, typeclass

__all__ = (
    'Monad',
    'MonadIO',
    'MonadIdentity',
    'MonadLambda',
    'MonadList',
    'MonadMaybe',
    'MonadParser',
)


a = TypeVar('a')

b = TypeVar('b')

m = TypeVar('m')

r = TypeVar('r')


@dataclass(frozen=True)
class Monad(Applicative[m], typeclass[m]):
    def bind(self, m : hkt[m, a], k : Lambda[a, hkt[m, b]], /) -> hkt[m, b]: ...

    def seq(self, m : hkt[m, a], k : hkt[m, b], /) -> hkt[m, b]:
        return self.bind(m, lambda _, /: k)


@dataclass(frozen=True)
class MonadIO(ApplicativeIO, Monad[IO]):
    async def bind(self, m : IO[a], k : Lambda[a, IO[b]], /) -> b:
        match await m:
            case x:
                return await k(x)


@dataclass(frozen=True)
class MonadIdentity(ApplicativeIdentity, Monad[Identity]):
    def bind(self, m : Identity[a], k : Lambda[a, Identity[b]], /) -> Identity[b]:
        match m:
            case Identity(x):
                return k(x)


@dataclass(frozen=True)
class MonadLambda(ApplicativeLambda[r], Monad[Lambda[r, _]]):
    def bind(self, f : Lambda[r, a], k : Lambda[a, Lambda[r, b]], /) -> Lambda[r, b]:
        return lambda r, /: k(f(r))(r)


@dataclass(frozen=True)
class MonadList(ApplicativeList, Monad[list]):
    def bind(self, xs : list[a], f : Lambda[a, list[b]], /) -> list[b]:
        return [y for x in xs for y in f(x)]


@dataclass(frozen=True)
class MonadMaybe(ApplicativeMaybe, Monad[Maybe]):
    def bind(self, m : Maybe[a], k : Lambda[a, Maybe[b]], /) -> Maybe[b]:
        match m:
            case Nothing():
                return Nothing()
            case Just(x):
                return k(x)


@dataclass(frozen=True)
class MonadParser(ApplicativeParser, Monad[Parser]):
    def bind(self, p : Parser[a], k : Lambda[a, Parser[b]], /) -> Parser[b]:
        return lambda s, /: [(y, s) for (x, s) in p(s) for (y, s) in k(x)(s)]
