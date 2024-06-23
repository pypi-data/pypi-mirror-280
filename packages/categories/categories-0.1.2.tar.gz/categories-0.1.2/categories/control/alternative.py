from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.control.applicative import Applicative, ApplicativeIO, ApplicativeList, ApplicativeMaybe, ApplicativeParser
from categories.data.maybe import Maybe, Nothing, Just
from categories.text.parser import Parser
from categories.type import IO, hkt, typeclass

__all__ = (
    'Alternative',
    'AlternativeIO',
    'AlternativeList',
    'AlternativeMaybe',
    'AlternativeParser',
)


a = TypeVar('a')

b = TypeVar('b')

f = TypeVar('f')


@dataclass(frozen=True)
class Alternative(Applicative[f], typeclass[f]):
    def unit(self, /) -> hkt[f, a]: ...

    def alt(self, x : hkt[f, a], y : hkt[f, a], /) -> hkt[f, a]: ...

    def some(self, v : hkt[f, a], /) -> hkt[f, list[a]]:
        return self.apply(self.map(lambda x, /: lambda xs, /: [x, *xs], v), self.many(v))

    def many(self, v : hkt[f, a], /) -> hkt[f, list[a]]:
        return self.alt(self.some(v), self.inject([]))


@dataclass(frozen=True)
class AlternativeIO(ApplicativeIO, Alternative[IO]):
    async def unit(self, /) -> a:
        raise Exception

    async def alt(self, m : IO[a], m_ : IO[a], /) -> a:
        try:
            return await m
        except BaseException:
            return await m_


@dataclass(frozen=True)
class AlternativeList(ApplicativeList, Alternative[list]):
    def unit(self, /) -> list[a]:
        return []

    def alt(self, xs : list[a], ys : list[a], /) -> list[a]:
        return xs + ys


@dataclass(frozen=True)
class AlternativeMaybe(ApplicativeMaybe, Alternative[Maybe]):
    def unit(self, /) -> Maybe[a]:
        return Nothing()

    def alt(self, m : Maybe[a], m_ : Maybe[a], /) -> Maybe[a]:
        match m:
            case Nothing():
                return m_
            case Just(_):
                return m


@dataclass(frozen=True)
class AlternativeParser(ApplicativeParser, Alternative[Parser]):
    def unit(self, /) -> Parser[a]:
        return lambda _, /: []

    def alt(self, p : Parser[a], q : Parser[a], /) -> Parser[a]:
        return lambda s, /: p(s) or q(s)

    def some(self, p : Parser[a], /) -> Parser[list[a]]:
        return lambda s, /: [([x, *xs], s) for (x, s) in p(s) for (xs, s) in self.many(p)(s)]

    def many(self, p : Parser[a], /) -> Parser[list[a]]:
        return self.alt(self.some(p), self.inject([]))
