import collections
from typing import Literal, cast

import pytest
from pytest import approx

import cw_enc.wave_blocks as wave_blocks
from cw_enc.parameters import Parameters


def testEmptySkirt() -> None:
    pms = cast(Parameters, collections.namedtuple("TestParameter", ["skirt_time"]))
    pms.skirt_time = 0
    assert wave_blocks.make_skirt(pms) == []


def testIllegalSkirt() -> None:
    pms = cast(
        Parameters,
        collections.namedtuple("TestParameter", ["skirt_time", "skirt_shape"]),
    )
    pms.skirt_time = 0.1
    pms.skirt_shape = cast(Literal["RC", "L"], "NoSuchShape")
    with pytest.raises(
        RuntimeError, match='Unsupported: "NoSuchShape" as skirt_shape.'
    ):
        wave_blocks.make_skirt(pms)


def testLSkirt() -> None:
    pms = cast(
        Parameters,
        collections.namedtuple(
            "TestParameter", ["skirt_time", "skirt_shape", "samples_per_second"]
        ),
    )
    pms.skirt_time = 0.099999999
    pms.skirt_shape = "L"
    pms.samples_per_second = 100
    assert wave_blocks.make_skirt(pms) == [approx(i * 0.1) for i in range(1, 10)]


def testRCSkirt() -> None:
    pass
