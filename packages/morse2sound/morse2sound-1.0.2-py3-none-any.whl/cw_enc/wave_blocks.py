import io
import math
import struct

from cw_enc.parameters import Parameters


class WaveGenerator:
    """Prepare to produce a sine wave out of a table, instead of calculating each value anew via the sine function."""

    def __init__(
        self, samples_per_second: int, f: int | float, f_delta: int | float
    ) -> None:
        if f_delta < 0.01:
            raise ValueError(f"f_delta {f_delta} is too strict, try >= 0.5 or so.")
        self.i = 0
        num_periods = 1
        while True:
            samples_per_periods: int = round(samples_per_second * num_periods / f)
            frequency_obtained = samples_per_second / samples_per_periods * num_periods
            if samples_per_periods > samples_per_second / 5:
                raise RuntimeError(
                    f"Too strict combination: f {f}±{f_delta} Hz at {samples_per_second} "
                    f"leads to {num_periods} periods in table, table length {samples_per_periods}."
                    f" (Frequency optained {frequency_obtained}). Hint: Raise f_delta."
                )
            if f - f_delta <= frequency_obtained <= f + f_delta:
                dt = 2 * math.pi * num_periods / samples_per_periods
                self.table: list[float] = [
                    math.sin(dt * i) for i in range(0, samples_per_periods)
                ]
                return
            num_periods += 1

    def next(self) -> float:
        result = self.table[self.i]
        self.i += 1
        if len(self.table) <= self.i:
            self.i = 0
        return result

    def create_reset_pointer(self) -> int:
        return self.i

    def reset(self, reset_pointer: int) -> None:
        self.i = reset_pointer


def make_one_sample(signal: float, pms: Parameters) -> bytes:
    # Convert signal (between -1 and +1 incl) into one little-endian sample 0 .. 2**16-1.
    # The sample contains the value as often as there are channels.
    s16 = round(pms.amplitude * signal)
    if pms.channels == 1:
        return struct.pack("<h", s16)
    elif pms.channels == 2:
        return struct.pack("<hh", s16, s16)
    else:
        raise RuntimeError("Unsupported: {} channels".format(pms.channels))


def make_silence(samples: int, pms: Parameters) -> bytes:
    """Create a certain number of samples of silence."""
    with io.BytesIO() as resultBuf:
        one_sample = make_one_sample(0.0, pms)
        for i in range(0, samples):
            resultBuf.write(one_sample)
        return resultBuf.getvalue()


def make_skirt(pms: Parameters) -> list[float]:
    """Create the skirt factors as number between 0.0 and 1.0."""
    if 0 < pms.skirt_time:
        if pms.skirt_shape == "RC":
            dt = math.pi / pms.samples_per_second / pms.skirt_time
            t = -math.pi + dt
            result = []
            while t < 0:
                result.append(0.5 * (1 + math.cos(t)))
                t += dt
            return result
        elif pms.skirt_shape == "L":
            dt = 1 / pms.samples_per_second / pms.skirt_time
            t = dt
            result = []
            while t < 1:
                result.append(t)
                t += dt
            return result
        else:
            raise RuntimeError(f'Unsupported: "{pms.skirt_shape}" as skirt_shape.')
    else:
        return []


class WaveBlocks:
    """All Morse code generated here consists of four symbols:

    - dit
    - dah
    - (inner-word) character separation space
    - word separation space

    Those are appended to .wav files (under the control of the PaddleMksnd class).
    """

    def __init__(self, dit: bytes, dah: bytes, csilence: bytes, iwsilence: bytes):
        self._dit = dit
        self._dah = dah
        self._csilence = csilence
        self._iwsilence = iwsilence

    @property
    def dit(self) -> bytes:
        """The bytes that produce the audio of one dit.

        This generally contains slow rise and slow fall skirts
        and is therefore longer than a dit time."""
        return self._dit

    @property
    def dah(self) -> bytes:
        """The bytes that produce the audio of one dah.

        This generally contains slow rise and slow fall skirts
        and is therefore longer than three dit times."""
        return self._dah

    @property
    def csilence(self) -> bytes:
        """The bytes that produce the audio of the silence
        that separates two characters in the same word.

        As dits and dahs are a little longer than norm Morse code,
        this is a bit shorter."""
        return self._csilence

    @property
    def iwsilence(self) -> bytes:
        """The bytes that produce the audio of the silence
        that separates two words.

        As dits and dahs are a little longer than norm Morse code,
        this is a bit shorter."""
        return self._iwsilence


def make_wave_blocks(pms: Parameters) -> WaveBlocks:
    """Function to generate the blocks of samples (bytes) we need."""

    with io.BytesIO() as ditBuf:
        with io.BytesIO() as dahBuf:
            wg = WaveGenerator(pms.samples_per_second, pms.f, pms.f_delta)
            skirt = make_skirt(pms)

            # In the following, we do a lot of bookkeeping and counting.
            # What we count are always the samples, not bytes.
            # (Bytes would depend on mono / stereo and stuff. We don't want to mess with that here.)

            # Rising skirt
            for i in range(0, len(skirt)):
                v = wg.next() * skirt[i]
                ditBuf.write(make_one_sample(v, pms))

            # Level "on" amplitude for one dit time minus half of the two skirts:
            regular_dit_num_of_samples = round(pms.dit_time() * pms.samples_per_second)
            for i in range(regular_dit_num_of_samples - len(skirt)):
                ditBuf.write(make_one_sample(wg.next(), pms))

            # Copy the work done thus far to the dot:
            dahBuf.write(ditBuf.getvalue())
            reset_point = wg.create_reset_pointer()
            num_of_samples_in_dah_copied_from_dit = regular_dit_num_of_samples

            # Falling skirt of the dit.
            for i in range(len(skirt) - 1, -1, -1):
                v = wg.next()
                ditBuf.write(make_one_sample(v * skirt[i], pms))

            # Fill in the rest of the full amplitude for the dah.
            wg.reset(reset_point)
            regular_dah_num_of_samples = round(pms.dah_time() * pms.samples_per_second)
            for i in range(
                regular_dah_num_of_samples - num_of_samples_in_dah_copied_from_dit
            ):
                dahBuf.write(make_one_sample(wg.next(), pms))

            # Falling skirt of the dah:
            for i in range(len(skirt) - 1, -1, -1):
                dahBuf.write(make_one_sample(wg.next() * skirt[i], pms))

            wanted_inner_char_silence_num_of_samples = regular_dit_num_of_samples - len(
                skirt
            )
            silence_after_sound = make_silence(
                wanted_inner_char_silence_num_of_samples, pms
            )
            ditBuf.write(silence_after_sound)
            dahBuf.write(silence_after_sound)

            cs_number_of_samples = round(
                pms.samples_per_second * (pms.csilence_time() - pms.dit_time())
            )
            # The paddle always inserts a character space after a character,
            # so we need only the additional length of the inter word space.
            iws_number_of_samples = (
                round(pms.samples_per_second * (pms.iwsilence_time() - pms.dit_time()))
                - cs_number_of_samples
            )

            return WaveBlocks(
                ditBuf.getvalue(),
                dahBuf.getvalue(),
                make_silence(cs_number_of_samples, pms),
                make_silence(
                    iws_number_of_samples,
                    pms,
                ),
            )
