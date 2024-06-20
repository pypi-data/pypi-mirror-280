import pathlib
import sys
import wave

import pytest

from cw_enc import driver


def test_driver(tmp_path: pathlib.Path) -> None:
    old_argv = list(sys.argv)
    try:
        sys.argv = ["driver.py"]
        cw_file = tmp_path / "plain_vanilla.wav"
        sys.argv.append("--intext")
        sys.argv.append("paris paris ")
        sys.argv.append("--out")
        sys.argv.append(str(cw_file))
        driver.drive()
        with wave.open(str(cw_file), mode="rb") as wr:
            assert wr.getnchannels() == 1
            assert wr.getsampwidth() == 2
            assert wr.getframerate() == 8000
            assert wr.getnframes() == 80000
    finally:
        sys.argv = old_argv


def test_driver_unmorseable_omit(tmp_path: pathlib.Path) -> None:
    old_argv = list(sys.argv)
    cw_file_nsc = tmp_path / "no_such_char.wav"
    try:
        sys.argv = ["driver.py"]
        sys.argv.append("--intext")
        sys.argv.append("paris! ")
        sys.argv.append("--on-unmorseable")
        sys.argv.append("x")
        sys.argv.append("--out")
        sys.argv.append(str(cw_file_nsc))
        driver.drive()

        with wave.open(str(cw_file_nsc), mode="rb") as wr:
            assert wr.getnchannels() == 1
            assert wr.getsampwidth() == 2
            assert wr.getframerate() == 8000
            assert wr.getnframes() == 40000
    finally:
        sys.argv = old_argv


def test_driver_unmorseable_replace(tmp_path: pathlib.Path) -> None:
    old_argv = list(sys.argv)
    cw_file_nsc = tmp_path / "exclam_turned_questionmark.wav"
    cw_file_replaced = tmp_path / "questionmark.wav"
    try:
        sys.argv = ["driver.py"]
        sys.argv.append("--intext")
        sys.argv.append("!")
        sys.argv.append("--on-unmorseable")
        sys.argv.append("?")
        sys.argv.append("--out")
        sys.argv.append(str(cw_file_nsc))
        driver.drive()
    finally:
        sys.argv = old_argv

    try:
        sys.argv = ["driver.py"]
        sys.argv.append("--intext")
        sys.argv.append("?")
        sys.argv.append("--on-unmorseable")
        sys.argv.append("?")
        sys.argv.append("--out")
        sys.argv.append(str(cw_file_replaced))
        driver.drive()
    finally:
        sys.argv = old_argv

    with wave.open(str(cw_file_nsc), mode="rb") as wr_nsc:
        with wave.open(str(cw_file_replaced), mode="rb") as wr_rep:
            num_of_frames = wr_nsc.getnframes()
            assert wr_rep.getnframes() == num_of_frames
            assert wr_nsc.readframes(num_of_frames) == wr_rep.readframes(num_of_frames)


def test_driver_unmorseable_balk(tmp_path: pathlib.Path) -> None:
    old_argv = list(sys.argv)
    cw_file_never_written = tmp_path / "never_written_file.wav"
    try:
        sys.argv = ["driver.py"]
        sys.argv.append("--intext")
        sys.argv.append("paris, oh! paris!")
        sys.argv.append("--on-unmorseable")
        sys.argv.append("False")
        sys.argv.append("--out")
        sys.argv.append(str(cw_file_never_written))
        with pytest.raises(
            KeyError, match='Character "!" not representable in Morse code.'
        ):
            driver.drive()
    finally:
        sys.argv = old_argv


def test_samplerate(tmp_path: pathlib.Path) -> None:
    old_argv = list(sys.argv)
    cw_file = tmp_path / "samplerate.wav"
    try:
        sys.argv = ["driver.py"]
        sys.argv.append("--intext")
        sys.argv.append("paris paris ")
        sys.argv.append("--samples-per-second")
        sys.argv.append("176400")
        sys.argv.append("--channels")
        sys.argv.append("2")
        sys.argv.append("--wpm")
        sys.argv.append("30")
        sys.argv.append("--out")
        sys.argv.append(str(cw_file))
        driver.drive()
        with wave.open(str(cw_file), mode="rb") as wr:
            assert wr.getnchannels() == 2
            assert wr.getsampwidth() == 2
            assert wr.getframerate() == 176400
            assert wr.getnframes() == 176400 * 4
    finally:
        sys.argv = old_argv


def test_farnsworth(tmp_path: pathlib.Path) -> None:
    old_argv = list(sys.argv)
    cw_file = tmp_path / "samplerate.wav"
    try:
        sys.argv = ["driver.py"]
        sys.argv.append("--intext")
        sys.argv.append("paris paris ")
        sys.argv.append("--samples-per-second")
        sys.argv.append("44100")
        sys.argv.append("--channels")
        sys.argv.append("2")
        sys.argv.append("--wpm")
        sys.argv.append("40")
        sys.argv.append("--farnsworth")
        sys.argv.append("24")
        sys.argv.append("--skirt-time")
        sys.argv.append("0.02")
        sys.argv.append("--out")
        sys.argv.append(str(cw_file))
        driver.drive()
        with wave.open(str(cw_file), mode="rb") as wr:
            assert wr.getnchannels() == 2
            assert wr.getsampwidth() == 2
            assert wr.getframerate() == 44100
            # FIXME: Does not come out precisely, but one sample deviation per "PARIS ". Why?
            assert 44100 * 5 - 2 <= wr.getnframes() <= 44100 * 5 + 2
    finally:
        sys.argv = old_argv
