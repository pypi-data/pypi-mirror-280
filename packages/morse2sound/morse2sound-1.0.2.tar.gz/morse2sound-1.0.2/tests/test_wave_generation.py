import collections
import math
from typing import Literal, cast

import pytest
from pytest import approx

import cw_enc.wave_blocks as wave_blocks
from cw_enc.parameters import Parameters


def testWaveGeneratorPlainVanilla() -> None:
    dut = wave_blocks.WaveGenerator(10000, 2500, 0.5)
    assert dut.next() == approx(0.0)
    assert dut.next() == approx(1.0)
    assert dut.next() == approx(0.0)
    assert dut.next() == approx(-1.0)
    assert dut.next() == approx(0.0)
    assert dut.next() == approx(1.0)
    assert dut.next() == approx(0.0)
    assert dut.next() == approx(-1.0)


def testWaveGeneratorTableOddF() -> None:
    # This is way too few samples, but makes easily calculated values.
    dut = wave_blocks.WaveGenerator(200, 150.0, 0.5)
    assert dut.next() == approx(0.0)
    assert dut.next() == approx(math.sin(1.5 * math.pi))
    assert dut.next() == approx(0.0)
    assert dut.next() == approx(math.sin(2.5 * math.pi))
    assert dut.next() == approx(0.0)
    assert dut.next() == approx(math.sin(1.5 * math.pi))
    assert dut.next() == approx(0.0)
    assert dut.next() == approx(math.sin(2.5 * math.pi))
    assert dut.next() == approx(0.0)
    assert dut.next() == approx(math.sin(1.5 * math.pi))
    assert dut.next() == approx(0.0)
    assert dut.next() == approx(math.sin(2.5 * math.pi))


def test_dit_and_dah_L() -> None:
    for channels in cast(list[Literal[1, 2]], [1, 2]):
        pms = Parameters(
            samples_per_second=10000,
            wpm=12,
            farnsworth_wpm=None,
            f=700,
            f_delta=12,
            channels=channels,
            skirt_time=0.01,
            skirt_shape="L",
        )
        dut = wave_blocks.make_wave_blocks(pms)

        assert len(dut.dit) == 2000 * 2 * pms.channels  # 100 ms dit + 100 ms silence
        assert len(dut.dah) == 4000 * 2 * pms.channels  # 300 ms dah + 100 ms silence

        assert len(dut.csilence) == 2000 * 2 * pms.channels
        # 300 ms minus 100 ms from previous dit or dah

        assert len(dut.iwsilence) == 4000 * 2 * pms.channels
        # 700 ms minus 100 ms from previous dit or dah minus 200 that we already have from the csilence

        wg = wave_blocks.WaveGenerator(pms.samples_per_second, pms.f, pms.f_delta)
        rising_skirt: list[int] = []
        for i in range(0, 100):
            rising_skirt.extend(
                wave_blocks.make_one_sample(wg.next() * (i + 1) / 100, pms)
            )

        assert len(rising_skirt) == 100 * 2 * pms.channels
        for i in range(0, 100 * 2 * pms.channels):
            assert dut.dit[i] == rising_skirt[i]

        silence_samples = wave_blocks.make_one_sample(0, pms)
        for silence_under_test, silence_start_index in cast(
            list[tuple[bytes, int]],
            [
                [dut.dit, 1100],
                [dut.dah, 3100],
                [dut.csilence, 0],
                [dut.iwsilence, 0],
            ],
        ):
            for i in range(
                silence_start_index, round(len(silence_under_test) / 2 / pms.channels)
            ):
                assert (
                    silence_under_test[
                        2 * pms.channels * i : 2 * pms.channels * (i + 1)  # noqa E203
                    ]
                    == silence_samples
                )


def test_dit_and_dah_RC() -> None:
    for channels in cast(list[Literal[1, 2]], [1, 2]):
        pms = Parameters(
            samples_per_second=10000,
            wpm=12,
            farnsworth_wpm=None,
            f=700,
            f_delta=12,
            channels=channels,
            skirt_time=0.01,
            skirt_shape="RC",
        )
        dut = wave_blocks.make_wave_blocks(pms)

        assert len(dut.dit) == 2000 * 2 * pms.channels  # 100 ms dit + 100 ms silence
        assert len(dut.dah) == 4000 * 2 * pms.channels  # 300 ms dah + 100 ms silence

        assert len(dut.csilence) == 2000 * 2 * pms.channels
        # 300 ms minus 100 ms from previous dit or dah

        assert len(dut.iwsilence) == 4000 * 2 * pms.channels
        # 700 ms minus 100 ms from previous dit or dah minus 200 that we already have from the csilence

        wg = wave_blocks.WaveGenerator(pms.samples_per_second, pms.f, pms.f_delta)
        rising_skirt: list[int] = []
        for i in range(0, 100):
            rising_skirt.extend(
                wave_blocks.make_one_sample(
                    wg.next() * (0.5 - 0.5 * math.cos(math.pi * (i + 1) / 100)), pms
                )
            )

        assert len(rising_skirt) == 100 * 2 * pms.channels
        for i in range(0, 100 * 2 * pms.channels):
            assert dut.dit[i] == rising_skirt[i]
            assert dut.dah[i] == rising_skirt[i]

        for i in range(100, 1000):
            one_sample = wave_blocks.make_one_sample(wg.next(), pms)
            for j in range(0, 2 * pms.channels):
                assert dut.dit[i * 2 * pms.channels + j] == one_sample[j]
                assert dut.dah[i * 2 * pms.channels + j] == one_sample[j]

        for i in range(1000, 1100):
            value = wg.next()
            dah_sample = wave_blocks.make_one_sample(value, pms)
            dit_sample = wave_blocks.make_one_sample(
                value * (0.5 - 0.5 * math.cos(math.pi * (1100 - i) / 100)), pms
            )
            for j in range(0, 2 * pms.channels):
                assert dut.dah[i * 2 * pms.channels + j] == dah_sample[j]
                assert dut.dit[i * 2 * pms.channels + j] == dit_sample[j]

        for i in range(1100, 3000):
            dah_sample = wave_blocks.make_one_sample(wg.next(), pms)
            for j in range(0, 2 * pms.channels):
                assert dut.dah[i * 2 * pms.channels + j] == dah_sample[j]

        for i in range(3000, 3100):
            dah_sample = wave_blocks.make_one_sample(
                wg.next() * (0.5 - 0.5 * math.cos(math.pi * (3100 - i) / 100)), pms
            )
            for j in range(0, 2 * pms.channels):
                assert dut.dah[i * 2 * pms.channels + j] == dah_sample[j]

        silence_samples = wave_blocks.make_one_sample(0, pms)
        for silence_under_test, silence_start_index in cast(
            list[tuple[bytes, int]],
            [
                [dut.dit, 1100],
                [dut.dah, 3100],
                [dut.csilence, 0],
                [dut.iwsilence, 0],
            ],
        ):
            for i in range(
                silence_start_index, round(len(silence_under_test) / 2 / pms.channels)
            ):
                assert (
                    silence_under_test[
                        2 * pms.channels * i : 2 * pms.channels * (i + 1)  # noqa E203
                    ]
                    == silence_samples
                )


def test_illegal_channels_are_rejected() -> None:
    pms = cast(
        Parameters, collections.namedtuple("TestParameter", ["amplitude", "channels"])
    )
    pms.amplitude = 2**15 - 1
    pms.channels = cast(Literal[1, 2], 3)
    with pytest.raises(RuntimeError, match="Unsupported: 3 channels"):
        wave_blocks.make_one_sample(0.5, pms)
