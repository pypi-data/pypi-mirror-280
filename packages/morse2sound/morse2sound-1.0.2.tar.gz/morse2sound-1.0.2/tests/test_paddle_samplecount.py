from cw_enc.paddle_samplecount import PaddleSampleCount


def test_dit_dah_count() -> None:
    dut = PaddleSampleCount(
        dit_samples=1, dah_samples=4, ci_silence_samples=16, iw_silence_samples=64
    )
    assert dut.count() == 0
    dut.dit()
    assert dut.count() == 1
    dut.csilence()
    assert dut.count() == 17
    dut.dah()
    assert dut.count() == 21
    dut.csilence()
    assert dut.count() == 37
    dut.dit()
    assert dut.count() == 38
    dut.csilence()
    assert dut.count() == 54
    dut.iwsilence()
    assert dut.count() == 118
