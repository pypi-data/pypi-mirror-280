from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from categories.control.alternative import Alternative, AlternativeIO, AlternativeList, AlternativeMaybe, AlternativeParser
from categories.control.monad import Monad, MonadIO, MonadList, MonadMaybe, MonadParser
from categories.data.maybe import Maybe, Nothing, Just
from categories.text.parser import Parser
from categories.type import IO, hkt, typeclass

__all__ = (
    'MonadPlus',
    'MonadPlusIO',
    'MonadPlusList',
    'MonadPlusMaybe',
    'MonadPlusParser',
)


a = TypeVar('a')

m = TypeVar('m')


@dataclass(frozen=True)
class MonadPlus(Alternative[m], Monad[m], typeclass[m]):
    def plus(self, x : hkt[m, a], y : hkt[m, a], /) -> hkt[m, a]:
        return self.alt(x, y)


@dataclass(frozen=True)
class MonadPlusIO(AlternativeIO, MonadIO, MonadPlus[IO]):
    async def plus(self, m : IO[a], m_ : IO[a], /) -> a:
        try:
            return await m
        except BaseException:
            return await m_


@dataclass(frozen=True)
class MonadPlusList(AlternativeList, MonadList, MonadPlus[list]): ...


@dataclass(frozen=True)
class MonadPlusMaybe(AlternativeMaybe, MonadMaybe, MonadPlus[Maybe]): ...


@dataclass(frozen=True)
class MonadPlusParser(AlternativeParser, MonadParser, MonadPlus[Parser]): ...
