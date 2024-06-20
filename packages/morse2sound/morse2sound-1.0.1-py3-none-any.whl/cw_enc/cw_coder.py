from typing import Callable

from cw_enc.paddle import Paddle


def raise_on_notmorseable_char(char: str) -> str:
    raise KeyError('Character "{}" not representable in Morse code.'.format(char))


def ignore_char(char: str) -> str:
    return "x"


def replace_char_with_questionmark(char: str) -> str:
    return "..--.."


class CWCoder:
    """Internal class that knows how to call dit and dah and so on, given a message character."""

    codelist = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        ":": "---...",
        "=": "-...-",
        "-": "-....-",
        "?": "..--..",
        ".": ".-.-.-",
        ",": "--..--",
        "(": "-.--.",
        ")": "-.--.-",
        "+": ".-.-.",
        "/": "-..-.",
        "@": ".--.-.",
    }

    def __init__(
        self,
        paddle: Paddle,
        on_missing: Callable[[str], str] = raise_on_notmorseable_char,
        codelist: dict[str, str] = codelist,
    ) -> None:
        self.paddle = paddle

        class Codelist(dict[str, str]):
            def __missing__(self, char: str) -> str:
                return on_missing(char)

        self.codelist = Codelist(codelist)

    def code(self, char: str, csilence: bool = True) -> None:
        if char == " " or char == "\n" or char == "\t":
            self.paddle.iwsilence()
        else:
            code = self.codelist[char.lower()]
            if code == "x":
                pass
            else:
                for dida in self.codelist[char.lower()]:
                    if dida == ".":
                        self.paddle.dit()
                    elif dida == "-":
                        self.paddle.dah()
                    else:
                        raise RuntimeError(
                            'Morse symbol "{}" is neither "." nor "-".'.format(dida)
                        )
                if csilence:
                    self.paddle.csilence()
