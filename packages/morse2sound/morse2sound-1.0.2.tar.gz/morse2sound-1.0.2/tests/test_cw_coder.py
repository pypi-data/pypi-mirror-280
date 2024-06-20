import pytest

import cw_enc.cw_coder as cw_coder
from cw_enc.paddle_cache import PaddleCache


def test_unforgiving_coder() -> None:
    with PaddleCache() as paddle:
        dut = cw_coder.CWCoder(paddle)
        for c in "Lorem Ipsum\ne\tt":
            dut.code(c)
        assert paddle.cmds == b".-.._---_.-._._--_ .._.--._..._..-_--_ ._ -_"
        with pytest.raises(
            KeyError, match='Character "!" not representable in Morse code.'
        ):
            dut.code("!")


def test_ignoring_coder() -> None:
    with PaddleCache() as paddle:
        dut = cw_coder.CWCoder(paddle, on_missing=cw_coder.ignore_char)
        for c in "Lorem Ipsum":
            dut.code(c)
        assert paddle.cmds == b".-.._---_.-._._--_ .._.--._..._..-_--_"
        dut.code("~")
        assert paddle.cmds == b".-.._---_.-._._--_ .._.--._..._..-_--_"


def test_questionmark_coder() -> None:
    with PaddleCache() as paddle:
        dut = cw_coder.CWCoder(
            paddle, on_missing=cw_coder.replace_char_with_questionmark
        )
        for c in "Lorem Ipsum":
            dut.code(c)
        assert paddle.cmds == b".-.._---_.-._._--_ .._.--._..._..-_--_"
        dut.code("~")
        assert paddle.cmds == b".-.._---_.-._._--_ .._.--._..._..-_--_..--.._"


def test_coder_raises_on_internal_error() -> None:
    with PaddleCache() as paddle:
        dut = cw_coder.CWCoder(paddle, on_missing=lambda c: "?")
        for c in "Lorem Ipsum":
            dut.code(c)
        assert paddle.cmds == b".-.._---_.-._._--_ .._.--._..._..-_--_"
        with pytest.raises(
            RuntimeError, match=r"Morse symbol \"\?\" is neither \"\.\" nor \"-\"\."
        ):
            dut.code("~")


def test_prosign() -> None:
    with PaddleCache() as paddle:
        dut = cw_coder.CWCoder(paddle)
        dut.code("S", csilence=False)
        dut.code("K")
        assert paddle.cmds == b"...-.-_"
