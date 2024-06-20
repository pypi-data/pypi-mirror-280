from types import TracebackType
from typing import Literal, Optional, Type

from cw_enc.paddle import Paddle


class PaddleCache(Paddle):
    """Internal class that forwards the stuff it had received to a bunch of other paddles, one after the other."""

    # Beware... this will close all the paddles in the list.
    def __init__(self, paddle_list: list[Paddle] = []) -> None:
        self.paddle_list = list(paddle_list)
        self.cmds = bytearray()

    def dit(self) -> None:
        self.cmds.append(46)  # b'.'[0]

    def dah(self) -> None:
        self.cmds.append(45)  # b'-'[0]

    def csilence(self) -> None:
        self.cmds.append(95)  # b'_'[0]

    def iwsilence(self) -> None:
        self.cmds.append(32)  # b' '[0]

    def __enter__(self) -> "PaddleCache":
        # We should not need to have this function,
        # but without, mypy somehow does not understand what we're trying to do.
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> Literal[False]:
        if exc_type is not None:
            return False
        for sp in self.paddle_list:
            with sp as sub_paddle:
                for cmd in self.cmds:
                    if cmd == 46:
                        sub_paddle.dit()
                    elif cmd == 45:
                        sub_paddle.dah()
                    elif cmd == 95:
                        sub_paddle.csilence()
                    elif cmd == 32:
                        sub_paddle.iwsilence()
                    else:
                        raise RuntimeError(
                            "Unhandled value (how did it get here?): {}".format(cmd)
                        )
        return False
