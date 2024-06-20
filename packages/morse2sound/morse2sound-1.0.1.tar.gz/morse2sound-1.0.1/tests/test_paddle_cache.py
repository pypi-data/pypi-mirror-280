from types import TracebackType
from typing import Literal, Optional, Type, cast

import pytest

from cw_enc.paddle import Paddle
from cw_enc.paddle_cache import PaddleCache


class BlubException(Exception):
    pass


def test_paddle_cache() -> None:
    class TestPaddle1(Paddle):
        def __init__(self) -> None:
            self.step = 0

        def dit(self) -> None:
            assert self.step == 0 or self.step == 4
            self.step += 1

        def dah(self) -> None:
            assert self.step == 2 or self.step == 7
            self.step += 1

        def csilence(self) -> None:
            assert self.step == 1 or self.step == 3 or self.step == 5
            self.step += 1

        def iwsilence(self) -> None:
            assert self.step == 6
            self.step += 1

        def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
        ) -> Literal[False]:
            assert self.step == 8
            self.step += 1
            return False

    tp1 = TestPaddle1()
    tp2 = TestPaddle1()
    pc = PaddleCache([tp1, tp2])
    with pc as paddle_cache:
        paddle_cache.dit()  # 1
        paddle_cache.csilence()  # 2
        paddle_cache.dah()  # 3
        paddle_cache.csilence()  # 4
        paddle_cache.dit()  # 5
        paddle_cache.csilence()  # 6
        paddle_cache.iwsilence()  # 7
        paddle_cache.dah()  # 8
        # 9
    assert tp1.step == 9
    assert tp2.step == 9


def test_paddle_inner_exception() -> None:

    class TestPaddle2(Paddle):
        def __init__(self) -> None:
            self.step = 0

        def dit(self) -> None:
            assert self.step == 0 or self.step == 4
            self.step += 1

        def dah(self) -> None:
            assert self.step == 2 or self.step == 7
            self.step += 1

        def csilence(self) -> None:
            assert self.step == 1 or self.step == 3 or self.step == 5
            self.step += 1

        def iwsilence(self) -> None:
            assert self.step == 6
            self.step += 1
            raise BlubException("örgs")

        def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
        ) -> Literal[False]:
            assert self.step == 8 or self.step == 7
            self.step += 1
            return super().__exit__(exc_type, exc_val, exc_tb)

    tp1 = TestPaddle2()
    tp2 = TestPaddle2()
    pc = PaddleCache([tp1, tp2])
    with pytest.raises(BlubException, match="örgs"):
        with pc as paddle_cache:
            paddle_cache.dit()  # 1
            paddle_cache.csilence()  # 2
            paddle_cache.dah()  # 3
            paddle_cache.csilence()  # 4
            paddle_cache.dit()  # 5
            paddle_cache.csilence()  # 6
            paddle_cache.iwsilence()  # 7
            paddle_cache.dah()  # 8
            # 9
    assert tp1.step == 8
    assert tp2.step == 0


def test_paddle_outer_exception() -> None:
    class TestPaddle3(Paddle):
        def __init__(self) -> None:
            self.step = 0

        def dit(self) -> None:
            assert self.step == 0 or self.step == 4
            self.step += 1

        def dah(self) -> None:
            assert self.step == 2 or self.step == 7
            self.step += 1

        def csilence(self) -> None:
            assert self.step == 1 or self.step == 3 or self.step == 5
            self.step += 1

        def iwsilence(self) -> None:
            assert self.step == 6
            self.step += 1

        def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
        ) -> Literal[False]:
            assert self.step == 8
            self.step += 1
            return False

    tp1 = TestPaddle3()
    tp2 = TestPaddle3()
    pc = PaddleCache([tp1, tp2])

    with pytest.raises(BlubException, match="Oh, no!"):
        with pc as paddle_cache:
            paddle_cache.dit()  # 1
            paddle_cache.csilence()  # 2
            paddle_cache.dah()  # 3
            paddle_cache.csilence()  # 4
            raise BlubException("Oh, no!")
    assert tp1.step == 0
    assert tp2.step == 0


def test_paddle_messed_up_internal_state() -> None:

    class TestPaddle4(Paddle):
        def __init__(self) -> None:
            self.step = 0

        def dit(self) -> None:
            assert self.step == 0 or self.step == 4
            self.step += 1

        def dah(self) -> None:
            assert self.step == 2 or self.step == 7
            self.step += 1

        def csilence(self) -> None:
            assert self.step == 1 or self.step == 3 or self.step == 5
            self.step += 1

        def iwsilence(self) -> None:
            assert self.step == 6
            self.step += 1

        def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
        ) -> Literal[False]:
            self.step += 1
            return False

    tp1 = TestPaddle4()
    tp2 = TestPaddle4()
    tp_l: list[Optional[Paddle]] = [tp1, tp2]
    pc = PaddleCache(cast(list[Paddle], tp_l))
    tp_l[0] = None
    tp_l[1] = None
    with pytest.raises(
        RuntimeError, match=r"Unhandled value \(how did it get here\?\): 100"
    ):
        with pc as paddle_cache:
            paddle_cache.dit()
            paddle_cache.csilence()
            paddle_cache.cmds.append(100)
            paddle_cache.dah()
    assert tp1.step == 3
    assert tp2.step == 0
