from abc import abstractmethod
from types import TracebackType
from typing import Literal, Optional, Type, TypeVar

T = TypeVar("T", bound="Paddle")


class Paddle:
    """Internal class that knows what to do with a dit, a dah, and such.

    Called "Paddle" after modern Morse keys that have two levers,
    one for dit and one for dah, which are also called paddles.

    Is also a context manager.
    """

    @abstractmethod
    def dit(self) -> None:
        pass

    @abstractmethod
    def dah(self) -> None:
        pass

    @abstractmethod
    def csilence(self) -> None:
        """Sound the silence that follows each character."""
        pass

    @abstractmethod
    def iwsilence(self) -> None:
        """Sound the additional silence that follows the csilence at the end of a word."""
        pass

    def __enter__(self: "Paddle") -> "Paddle":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> Literal[False]:
        return False
