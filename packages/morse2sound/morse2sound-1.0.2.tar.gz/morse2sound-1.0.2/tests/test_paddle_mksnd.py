from io import BytesIO

from cw_enc.paddle_mksnd import PaddleMksnd
from cw_enc.wave_blocks import WaveBlocks


def test_dit_dah_produce() -> None:
    with BytesIO() as consumer:

        class Catcher:
            def write(self, write_me: bytes) -> None:
                consumer.write(write_me)

        dut = PaddleMksnd(
            WaveBlocks(b"dit ", b"dah ", b"csilence ", b"iwsilence "),
            consumer=Catcher(),
        )
        assert consumer.getvalue() == b""
        dut.dit()
        assert consumer.getvalue() == b"dit "
        dut.csilence()
        assert consumer.getvalue() == b"dit csilence "
        dut.dah()
        assert consumer.getvalue() == b"dit csilence dah "
        dut.csilence()
        assert consumer.getvalue() == b"dit csilence dah csilence "
        dut.dit()
        assert consumer.getvalue() == b"dit csilence dah csilence dit "
        dut.csilence()
        assert consumer.getvalue() == b"dit csilence dah csilence dit csilence "
        dut.iwsilence()
        assert (
            consumer.getvalue() == b"dit csilence dah csilence dit csilence iwsilence "
        )
