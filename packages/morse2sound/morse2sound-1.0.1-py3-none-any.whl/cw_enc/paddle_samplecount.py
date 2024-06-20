from cw_enc.paddle import Paddle


class PaddleSampleCount(Paddle):
    """This internal class can count how many samples the wav files will have."""

    def __init__(
        self,
        dit_samples: int,
        dah_samples: int,
        ci_silence_samples: int,
        iw_silence_samples: int,
    ) -> None:
        self._count = 0
        self.dit_samples = dit_samples
        self.dah_samples = dah_samples
        self.ci_silence_samples = ci_silence_samples
        self.iw_silence_samples = iw_silence_samples

    def dit(self) -> None:
        self._count += self.dit_samples

    def dah(self) -> None:
        self._count += self.dah_samples

    def csilence(self) -> None:
        self._count += self.ci_silence_samples

    def iwsilence(self) -> None:
        self._count += self.iw_silence_samples

    def count(self) -> int:
        return self._count
