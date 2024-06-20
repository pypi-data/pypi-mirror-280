from typing import Literal, cast

import pytest
from pytest import approx

from cw_enc.parameters import ParameterError, Parameters


def testSlowNormCW() -> None:
    dut = Parameters()
    assert dut.wpm == approx(12.0)
    assert dut.farnsworth_wpm == approx(12.0)
    assert dut.dit_time() == approx(0.1)
    assert dut.dah_time() == approx(0.3)
    assert dut.csilence_time() == approx(0.3)
    assert dut.iwsilence_time() == approx(0.7)
    # "PARIS "
    assert (
        10 * dut.dit_time()
        + 4 * dut.dah_time()
        + 9 * dut.dit_time()
        + 4 * dut.csilence_time()
        + dut.iwsilence_time()
        == approx(5.0)
    )


def testfarnsworthCW() -> None:
    dut = Parameters(farnsworth_wpm=4)
    assert dut.wpm == approx(12.0)
    assert dut.dit_time() == approx(0.1)
    assert dut.dah_time() == approx(0.3)
    assert dut.csilence_time() * 7 == approx(dut.iwsilence_time() * 3)
    # "PARIS "
    assert (
        10 * dut.dit_time()
        + 4 * dut.dah_time()
        + 9 * dut.dit_time()
        + 4 * dut.csilence_time()
        + dut.iwsilence_time()
        == approx(15.0)
    )


def testArgumentChecking() -> None:
    with pytest.raises(ParameterError, match="farnsworth"):
        Parameters(farnsworth_wpm=0)

    with pytest.raises(ParameterError, match="farnsworth"):
        Parameters(farnsworth_wpm=12.1)

    with pytest.raises(ParameterError, match="samples_per_second"):
        Parameters(samples_per_second=0)

    with pytest.raises(ParameterError, match="amplitude"):
        Parameters(amplitude=2**15)

    with pytest.raises(ParameterError, match="channels"):
        Parameters(channels=cast(Literal[1, 2], 3))

    with pytest.raises(ParameterError, match="wpm"):
        Parameters(wpm=0)

    with pytest.raises(ParameterError, match="f.+samples_per_second"):
        Parameters(f=5000)

    with pytest.raises(ParameterError, match="f_delta"):
        Parameters(f_delta=0)

    with pytest.raises(ParameterError, match="skirt_time"):
        Parameters(skirt_time=0.101)

    with pytest.raises(ParameterError, match="skirt_shape"):
        Parameters(skirt_shape=cast(Literal["RC", "L"], "Lorem"))


def testParametersGetThere() -> None:
    dut = Parameters(
        samples_per_second=10000,
        amplitude=5000,
        channels=2,
        wpm=20,
        f=900,
        f_delta=50,
        skirt_time=6e-3,
        skirt_shape="L",
    )
    assert dut.samples_per_second == 10000
    assert dut.amplitude == 5000
    assert dut.channels == 2
    assert dut.wpm == approx(20)
    assert dut.f == approx(900)
    assert dut.f_delta == approx(50)
    assert dut.skirt_time == approx(6e-3)
    assert dut.skirt_shape == "L"
