from subprocess import run
from util import Lang, Colour


# Function to translate the text from the source language to the target language
def translate(text: str, lang: Lang) -> str:
    cmd = ["tl", "--from", lang._from, "--to", lang._to, text]
    res = run(cmd, capture_output=True)
    # Check if the translation was not successful and exit with its error
    if res.returncode != 0:
        exit(
            f"{Colour.RED}[ERROR]{Colour.NC} Translation failed with error:\n -> {_out_to_str(res.stderr)}"
        )
    # Otherwise return the output as a string
    else:
        return _out_to_str(res.stdout)


# Convert bytes to string and trim last char
def _out_to_str(out: bytes) -> str:
    return out.decode()[:-1]
