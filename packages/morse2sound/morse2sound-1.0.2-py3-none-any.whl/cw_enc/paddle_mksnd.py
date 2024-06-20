from typing import Protocol

from cw_enc.paddle import Paddle
from cw_enc.wave_blocks import WaveBlocks


class HasWrite(Protocol):
    def write(self, write_me: bytes) -> None: ...


class PaddleMksnd(Paddle):
    """This internal class stiches together stuff to be written to something that has a write method."""

    def __init__(self, what_to_write: WaveBlocks, consumer: HasWrite) -> None:
        self.what_to_write = what_to_write
        self.consumer = consumer

    def dit(self) -> None:
        self.consumer.write(self.what_to_write.dit)

    def dah(self) -> None:
        self.consumer.write(self.what_to_write.dah)

    def csilence(self) -> None:
        self.consumer.write(self.what_to_write.csilence)

    def iwsilence(self) -> None:
        self.consumer.write(self.what_to_write.iwsilence)
