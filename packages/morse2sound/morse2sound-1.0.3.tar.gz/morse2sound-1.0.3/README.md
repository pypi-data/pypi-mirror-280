# Morse2sound

## What can I do with this?

From some text, produce a sound file that contains that text, encoded
in Morse code.

## Background

### What's this Morse code thing?

Fast message transport via telegraphy was one of the first practical
uses of electricity, dating back to the middle of the 18th century.

[Samuel F. B. Morse](https://en.wikipedia.org/wiki/Samuel_Morse)
originally devised a scheme to transmit numbers via electric pulses,
with a code book that allowed translation of words to those numbers
and back.  Later, his assistant [Alfred
L. Vail](https://en.wikipedia.org/wiki/Alfred_Vail) improved on this
by coding single letters, so the code book became obsolete.  He used
short, long, longer, and extra long impulses.  His original method is
still remembered as [American Morse
Code](https://en.wikipedia.org/wiki/American_Morse_code), although it
sees little use.  This was again improved by [Friedrich
C. Gerke](https://en.wikipedia.org/wiki/Friedrich_Clemens_Gerke), who
simplified from four different impulse lengths to just two.  Gerke's
code is virtually identical to what is nowadays known as International
Morse Code.  In 1865, an international treaty established the
[ITU](https://www.itu.int/en/Pages/default.aspx) as the first
multinational standards organization, with the purpose of facilitating
cross-border transport of messages.  That same [1865
treaty](http://handle.itu.int/11.1004/020.1000/5.1.61.fr.200) also
formalized Gerke's version of the Morse code.  The coding of the
letters a-z and the digits 0-9 have remained unchanged since then, but
other things like punctuation indeed have seen some changes.  The ITU
still exists and to this day standardizes the [international Morse
code](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf),
among many other things.

### Is anybody still using Morse telegraphy?

Morse telegraphy is still extensively used by certain sections of the
HAM [amateur radio](https://en.wikipedia.org/wiki/Amateur_radio)
community. For obscure historical/technical reasons, Morse telegraphy
is generally designated as "CW".

CW is ubiquitous.  On an everyday basis, any CW-capable short wave
receiver (such as [Twente Web-SDR](http://websdr.ewi.utwente.nl:8901/)
available on the internet) is likely to pick up CW signals if tuned
through the designated telegraphy ranges, e.g., 7000-7040 kHz.  CW
sees extensive use among DXers (radio amateurs trying to reach rare
far-away places), in contests (radio amateur competitions), and by the
"home-brew" community (radio amateurs constructing their own
equipment).  By its supporters, CW is considered an enjoyable mode of
operation.

## Usage

### What does this software do?

It takes text and produces, as a sound file or stream, a Morse encoded
version of that text.

The output format is that of
[`.wav`](https://en.wikipedia.org/wiki/WAV) files.

### Basic usage

```shell
morse2sound --in message.txt --wpm 12 --out message.wav
```

For more info, do `morse2sound --help` or `morse2sound -h` .


### Character set

The international Morse code.

## Remarks

## Installation

Make sure when you say `python3`, then a resonably recent version of
Python comes up.  In particular, `python3 --version` should give a
3.10.something or later version.

_This software could be easily backported to 3.9 or 3.8, it's only
typing hints that require 3.10 or better.  (Previous published
versions also needed 3.10 or better, but claim to make do with 3.8 or
3.9.  This was a bug.  It has been fixed with 1.0.3: The software now
correctly says it needs Python>=3.10.)_

I suggest you create and activate a `venv`.  On Linux:

    python3 -m venv venv
    . venv/bin/activate

### Install

    pip install morse2sound

### Compression

The `.wav` files generated compress quite well, with the compression
algorithm of your choice, `zip` or something.

## Contributing

Have `git` installed.

```shell
git clone https://gitlab.com/4ham/morse2sound.git
```

Change to the directory `morse2sound` that was created by the above.

Create and activate a virtual environment as per the
[documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
pertaining to your OS.

Then:

```shell
pip install -r requirements_test.frozen
./lint.py
```

Do your changes and repeat that `python ./lint.py` part in your branch
before starting a pull request as usual towards the
[repository](https://gitlab.com/4ham/morse2sound).

## To run locally

```shell
PYTHONPATH=$(pwd)/src python src/cw_enc/driver.py -h
```

## To build locally

In an activated
[virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments):

```shell
pip install --upgrade build
rm -rf dist build morse2sound.egg-info
python -m build
```

To install what you built:

```shell
pip install dist/morse2sound-*-py3-none-any.whl
```

## To upload

This is useful only for the maintainer:

Extended tests with `pip install doit && doit --verbosity 2` .

* Edit the version in `pyproject.toml`
* `git tag -s vx.y.z`
* `git push origin --tags`

```shell
pip install --upgrade build twine
rm -rf dist build src/morse2sound.egg-info
python -m build
python -m twine upload dist/*
```
