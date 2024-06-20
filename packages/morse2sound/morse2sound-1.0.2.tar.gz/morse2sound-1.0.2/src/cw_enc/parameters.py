from typing import Literal


class ParameterError(Exception):
    def __init__(self, what: str, value: str | int | float):
        super().__init__('Value "{}" not allowed for parameter {}'.format(value, what))


class Parameters:
    """A data container class that keeps all the parameters needed to generate sound for dit and dah."""

    def __init__(
        self,
        samples_per_second: int = 8000,
        amplitude: float | int = 2**15 - 1,
        channels: Literal[1] | Literal[2] = 1,
        wpm: int | float = 12.0,
        farnsworth_wpm: None | int | float = None,
        f: int | float = 700,
        f_delta: int | float = 10,
        skirt_time: float = 5e-3,
        skirt_shape: Literal["RC"] | Literal["L"] = "RC",
    ) -> None:
        """Parameters:
        samples_per_second: An integer. Value frequently used for high fidelity: 44100. Default: 8000
        amplitude: A positive integer up to 2 ** 15 - 1 (the default), governing the loudness.
        channels: An integer. May be either 1 or 2. Default: 1.
        wpm: Words ("Paris") per minute. Multiply with 5 to get characters per minute. Default: 12
        farnsworth_wpm: None, or the slower resulting speed from additional Farnsworth sliences.
        f: Positive float. NF frequency in Hz you want generated. Typical and default value 700.
        f_delta: Positive float. How many Hz the frequency actually used may deviate from f. Default value 10.
        skirt_time: Non-negative float. How many seconds the tone gets to build up or cease. Default value 5e-3.
        skirt_shape: Either "RC" (default) for raised cosine shaping or "L" for linear shaping.

        Raises cw_get.parameters.ParameterError if the value does not fit.

        Farnsworth timing is calculated as suggested by the ARRL's suggestion in:
        "A Standard for Morse Timing Using the Farnsworth Technique" by Jon Bloom, KE3Z, ARRL Laboratory,
        QEX April 1990, page 8.

        The ideas are:

        - character as in norm speed
        - inner word spacing extended to a total spacing of t_c
        - between word spacing extended to a total spacing of t_w
        - tw = 7/3 t_c
        - total length of "PARIS " is same as with norm speed s (what we call farnsworth_wpm)

        The calculation: The 50 units of "PARIS " consist of 31 units of original speed c (what we call wpm here).
        The other 19 units need to be prolonged.

        A unit at speed c is 1.2 / c, so we have 31 times that, 37.2 / c, which is fixed.
        The whole thing needs to be slower, take time of 50 * (1.2 / s) = 60 / s seconds.

        So, each of the 19 remaining units needs to take (60 / s -  37.2 / c) seconds.
        Three of these for inner-word, seven of these for between words.

        For plausibility: If s == c, then 60 / c - 37.2 / c = 22.8 / c = 19 * 1.2 / c
        """
        if samples_per_second <= 0:
            raise ParameterError("samples_per_second", samples_per_second)
        self.samples_per_second = samples_per_second

        if amplitude < 0 or 2**15 - 1 < amplitude:
            raise ParameterError("amplitude", amplitude)
        self.amplitude = amplitude

        if 1 != channels and 2 != channels:
            raise ParameterError("channels", channels)
        self.channels = channels

        if wpm <= 0:
            raise ParameterError("wpm", wpm)
        self.wpm = wpm

        if farnsworth_wpm is not None and (
            wpm <= farnsworth_wpm or farnsworth_wpm <= 0
        ):
            raise ParameterError(
                f"farnsworth_wpm (with character speed {wpm} wpm)",
                farnsworth_wpm,
            )
        self.farnsworth_wpm = farnsworth_wpm if farnsworth_wpm is not None else wpm

        if f <= 0 or 0.5 * samples_per_second <= f:
            raise ParameterError(
                "f (with samples_per_second = {})".format(samples_per_second), f
            )
        self.f = f

        if f_delta <= 0:
            raise ParameterError("f_delta", f_delta)
        self.f_delta = f_delta

        if skirt_time < 0.0 or self.dit_time() < skirt_time:
            raise ParameterError(
                f"skirt_time (given wpm and farnsworth)"
                f" is negative or longer than dot time ({self.dit_time()} s).",
                skirt_time,
            )
        self.skirt_time = skirt_time

        if skirt_shape not in ["RC", "L"]:
            raise ParameterError("skirt_shape", skirt_shape)
        self.skirt_shape = skirt_shape

    def dit_time(self) -> float:
        """Theoretical duration of a dit (without additional duration needed for skirts).

        Also, duration of the silence within a character (the skirt will extend into this, but we don't care).
        """
        return 1.2 / self.wpm

    def dah_time(self) -> float:
        """Theoretical duration of a dah (again, without additional duration needed for skirts)."""
        return 3 * self.dit_time()

    def iwsilence_time(self) -> float:
        """Theoretical duration of the inter-word silence, again, without skirts and stuff.

        This takes into account any Farnsworth spacing.
        """
        return 7 / 19 * (60 / self.farnsworth_wpm - 37.2 / self.wpm)

    def csilence_time(self) -> float:
        """Theoretical duration of the between-character silence inside a word, without skirts and stuff.

        This takes into account any Farnsworth spacing.
        """
        return 3 / 19 * (60 / self.farnsworth_wpm - 37.2 / self.wpm)
