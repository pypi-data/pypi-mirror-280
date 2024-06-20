import argparse

import cw_enc


def drive() -> None:
    """This driver just does the argument parsing.

    If you want to use this as a library, check cw_enc.cw_enc .
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--intext", help="text to encode, " "provided directly via command line"
    )
    parser.add_argument("--infile", help="text to encode, provided via a text file.")
    parser.add_argument(
        "--on-unmorseable",
        help="what to do when characters do not exist "
        "in ITU's international Morse code: "
        '"False" for aborting, '
        '"?" for replacing with "?", '
        '"x" for silently ignoring'
        'default "?"',
        choices=["False", "?", "x"],
        default="?",
    )
    parser.add_argument(
        "--out",
        help='output .wav file name, or "-" for stdout. Default "morse2sound.wav".',
        default="morse2sound.wav",
    )
    parser.add_argument(
        "--samples-per-second",
        help="samples per seconds for output file, " "default 8000",
        default=8000,
        type=int,
    )
    parser.add_argument(
        "--amplitude",
        help="amplitude used by output file, "
        "default 32766, which is also the maximum",
        default=32766,
        type=int,
    )
    parser.add_argument(
        "--channels",
        help="channels in output file, default 1 (mono)",
        default=1,
        choices=[1, 2],
        type=int,
    )
    parser.add_argument(
        "--wpm",
        help="speed of output in words per minute (Paris), "
        "default 12, need not be integer",
        default=12,
        type=float,
    )
    parser.add_argument(
        "--freq",
        help="frequency of produced tone, default 700 Hz",
        type=float,
        default=700,
    )
    parser.add_argument(
        "--freq_delta_max",
        help="allowed deviation of produced tone frequency, " "default 10 Hz",
        default=10,
        type=float,
    )
    parser.add_argument(
        "--farnsworth",
        help="Farnsworth slower speed in wpm, at most or slower than --wpm, default None for no Farnsworth slowdown",
        required=False,
        type=float,
    )
    parser.add_argument(
        "--skirt-time",
        help="rise and fall time in seconds, default 0.005",
        default=5e-3,
        type=float,
    )
    parser.add_argument(
        "--skirt-shape",
        help="shape of rise and fall, "
        "default RC (raised cosine), other option L (linear)",
        default="RC",
        choices=["RC", "L"],
    )

    args = parser.parse_args()
    cw_enc.cw_enc(
        intext=args.intext,
        infile=args.infile,
        on_unmorseable=args.on_unmorseable,
        out=args.out,
        samples_per_second=args.samples_per_second,
        amplitude=args.amplitude,
        channels=args.channels,
        wpm=args.wpm,
        farnsworth_wpm=args.farnsworth,
        f=args.freq,
        f_delta=args.freq_delta_max,
        skirt_time=args.skirt_time,
        skirt_shape=args.skirt_shape,
    )


if __name__ == "__main__":
    drive()
