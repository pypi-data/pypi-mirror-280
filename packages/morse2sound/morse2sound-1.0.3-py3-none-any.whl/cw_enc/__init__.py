import sys
import wave
from types import TracebackType
from typing import IO, Literal, Optional, Type

from cw_enc.cw_coder import (
    CWCoder,
    ignore_char,
    raise_on_notmorseable_char,
    replace_char_with_questionmark,
)
from cw_enc.paddle_cache import PaddleCache
from cw_enc.paddle_mksnd import PaddleMksnd
from cw_enc.paddle_samplecount import PaddleSampleCount
from cw_enc.parameters import ParameterError, Parameters
from cw_enc.wave_blocks import make_wave_blocks


def cw_enc(
    intext: str = "Hello, world!",
    infile: Optional[str] = None,
    on_unmorseable: str = "?",
    out: str = "cwenc_out.wav",
    samples_per_second: int = 8000,
    amplitude: float | int = 2**15 - 2,
    channels: Literal[1] | Literal[2] = 1,
    wpm: int | float = 12.0,
    farnsworth_wpm: None | int | float = None,
    f: int | float = 700,
    f_delta: int | float = 1,
    skirt_time: float = 5e-3,
    skirt_shape: Literal["RC", "L"] = "RC",
) -> None:
    """The main driver program to produce Morse code .wav - files from characters."""

    if infile is not None and intext is not None:
        raise ParameterError("intext (when infile is also set)", intext)
    elif intext is not None:
        text = intext
    elif infile is not None:
        with open(infile) as inf:
            text = inf.read()
    else:
        raise FileNotFoundError(
            f"No text specified to convert to sound. Try {sys.argv[0]} -h"
        )

    pms = Parameters(
        samples_per_second=samples_per_second,
        amplitude=amplitude,
        channels=channels,
        wpm=wpm,
        farnsworth_wpm=farnsworth_wpm,
        f=f,
        f_delta=f_delta,
        skirt_time=skirt_time,
        skirt_shape=skirt_shape,
    )

    binout: str | IO[bytes]
    if out == "-":
        binout = sys.stdout.buffer
    else:
        binout = out

    with wave.open(binout, mode="wb") as wavout:
        wavout.setnchannels(pms.channels)
        wavout.setsampwidth(2)
        wavout.setframerate(pms.samples_per_second)

        # We will have a "paddle" that is given dits, dahs, between-character spaces, and between-words spaces.

        # Waveblock, containing pre-canned byte sequence for those four.
        wb = make_wave_blocks(pms)

        class WriteWavData:
            """Glue code: A simple object that has a write() method expecting bytes."""

            def write(self, b: bytes) -> None:
                wavout.writeframesraw(b)

        # The paddle that actually does the "heavy lifting", writing the data to the file.
        paddle_write_data = PaddleMksnd(what_to_write=wb, consumer=WriteWavData())

        # But first, deal with a complication: .wav files want to know how long they're going to be.
        class WriteWavHeader(PaddleSampleCount):
            """A subclass of Paddle that can count how many samples will be written."""

            def __exit__(
                self,
                exc_type: Optional[Type[BaseException]],
                exc_val: Optional[BaseException],
                exc_tb: Optional[TracebackType],
            ) -> Literal[False]:
                # On close, write the number of samples to the wav file:
                wavout.setnframes(self._count)
                return super().__exit__(exc_type, exc_val, exc_tb)

        paddle_write_header = WriteWavHeader(
            dit_samples=int(len(wb.dit) / pms.channels / 2),
            dah_samples=int(len(wb.dah) / pms.channels / 2),
            ci_silence_samples=int(len(wb.csilence) / pms.channels / 2),
            iw_silence_samples=int(len(wb.iwsilence) / pms.channels / 2),
        )

        # We go through the entire message twice:
        # First time for sample counting, secondly for real writing of the data.
        #
        # This is what a PaddleCache can do for us:
        # It patiently stores all the information given to it, until it is closed.
        # When it is closed (as a context manager), it will replay that information
        # on each of the paddles handed in, in order, one after the other.
        with PaddleCache([paddle_write_header, paddle_write_data]) as paddle:
            # Someone needs to convert the morse code to strings of dits and dahs
            # and hand those over to the paddle.
            # That is what a CWCoder does.
            if on_unmorseable == "False":
                unmorseable_character_strategy = raise_on_notmorseable_char
            elif on_unmorseable == "?":
                unmorseable_character_strategy = replace_char_with_questionmark
            elif on_unmorseable == "x":
                unmorseable_character_strategy = ignore_char
            else:
                raise ParameterError("on_unmorseable", on_unmorseable)
            coder = CWCoder(paddle=paddle, on_missing=unmorseable_character_strategy)
            for c in text:
                coder.code(c)

    # For good luck and stability:
    if out == "-":
        sys.stdout.buffer.flush()
