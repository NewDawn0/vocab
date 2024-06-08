# Man I miss structs and struct packing
# A wrapper which namespaces _from and _to for organisation purposes
class Lang:
    def __init__(self, _from: str, _to: str) -> None:
        self._from = _from
        self._to = _to


# A wrapper packing all the colours together
class Colour:
    BLUE = "\x1b[36;1m"
    GREEN = "\x1b[32;1m"
    NC = "\x1b[0m"
    RED = "\x1b[31;1m"
    YELLOW = "\x1b[33;1m"


# A print implementation which prints on the same line but first clears it
class ClearPrint:
    def __init__(self) -> None:
        self.last_line_len = 0

    def print(self, to_print: str) -> None:
        print(" " * self.last_line_len, end="\r")
        self.last_line_len = len(to_print)
        print(to_print, end="\r")
