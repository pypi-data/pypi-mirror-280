import collections
import struct
from typing import cast

import cw_enc.wave_blocks as wave_blocks
from cw_enc.parameters import Parameters


def test_float2sample() -> None:
    pms_raw = collections.namedtuple("pms_raw", ["amplitude", "channels"])
    pms_raw.amplitude = 2**15 - 1
    pms_raw.channels = 1
    pms = cast(Parameters, pms_raw)
    assert wave_blocks.make_one_sample(0.0, pms) == struct.pack("<h", 0)
    assert wave_blocks.make_one_sample(0.5, pms) == struct.pack("<h", 2**14)
    assert wave_blocks.make_one_sample(-1.0, pms) == struct.pack("<h", -(2**15) + 1)
    assert wave_blocks.make_one_sample(1.0, pms) == struct.pack("<h", 2**15 - 1)


def test_low_amplitude_two_channels() -> None:
    pms_raw = collections.namedtuple("pms_raw", ["amplitude", "channels"])
    pms_raw.amplitude = 1000
    pms_raw.channels = 2
    pms = cast(Parameters, pms_raw)
    assert wave_blocks.make_one_sample(0.0, pms) == struct.pack("<hh", 0, 0)
    assert wave_blocks.make_one_sample(0.5, pms) == struct.pack("<hh", 500, 500)
    assert wave_blocks.make_one_sample(-1.0, pms) == struct.pack("<hh", -1000, -1000)
    assert wave_blocks.make_one_sample(1.0, pms) == struct.pack("<hh", 1000, 1000)


def test_silence() -> None:
    pms = collections.namedtuple("pms", ["amplitude", "channels"])
    pms.amplitude = 1000
    pms.channels = 2
    s3 = wave_blocks.make_silence(3, cast(Parameters, pms))
    assert len(s3) == 12
    assert s3 == struct.pack("<hhhhhh", 0, 0, 0, 0, 0, 0)
