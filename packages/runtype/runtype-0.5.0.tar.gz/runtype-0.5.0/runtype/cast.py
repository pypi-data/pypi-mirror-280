#
# NOTE: Currently doesn't work because we don't support dispatch on generics
#       Type[X] gets cached as <type>
#

import typing as t
from contextlib import suppress
from datetime import datetime

from . import datetime_parse
from . import multidispatch, multidispatch_final
from .base_types import SumType

class CastFailed(Exception): ...


@multidispatch
def cast(obj: str, to_type: t.Type[int]):
    try:
        return int(obj)
    except ValueError:
        raise CastFailed()

@multidispatch
def cast(obj: str | int, to_type: t.Type[float]):
    try:
        return float(obj)
    except ValueError:
        raise CastFailed()

@multidispatch
def cast(obj: str, to_type: t.Type[datetime]):
    try:
        return datetime_parse.parse_datetime(obj)
    except datetime_parse.DateTimeError:
        raise CastFailed()

@multidispatch
def cast(obj, to_type: t.Type[object]):
    return obj

@multidispatch
def cast(obj: str, to_type: t.Type[SumType]):
    for t in to_type.types:
        with suppress(TypeError):
            return cast(obj, t)

    raise CastFailed()

@multidispatch_final
def cast(obj, to_type):
    raise CastFailed()


def test():
    # print("@"* 100)
    # breakpoint()
    # assert cast("1", str) == 1
    breakpoint()
    assert cast("1.5", float) == 1.5
    assert isinstance(cast("1", int), int)
    # assert cast("1", object) == 1
    # assert cast("a", int) == 1

if __name__ == '__main__':
    test()