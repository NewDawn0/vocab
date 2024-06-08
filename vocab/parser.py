from os import path
from translate import translate
from util import Lang, Colour, ClearPrint


class File:
    def __init__(
        self, path: str, sep: str, uses_tl: bool, lang: Lang, switch: bool
    ) -> None:
        self.path = path
        self.sep = sep
        self.uses_tl = uses_tl
        self.contents = self._read()
        self.lang = lang
        self.switch = switch
        self._validate_contents()

    # Check if the path exists
    def _validate_path(self) -> None:
        if path.exists(self.path):
            return
        exit(
            f"{Colour.RED}[ERROR]{Colour.NC} Wordlist file `{self.path}` does not exist"
        )

    # Read file contents
    def _read(self) -> list[str]:
        self._validate_path()
        contents: list[str] = list()
        with open(self.path, "r") as f:
            for line in f:
                # Trim whitespace
                stripped = line.strip()
                # Skip empty lines
                if not stripped:
                    continue
                contents.append(stripped)
        return contents

    # Check if the contents are valid
    def _validate_contents(self) -> None:
        errors: list[str] = list()
        amount_of_seps = 0 if self.uses_tl else 1
        # We need to read from the file again as the contents skips empty lines so the error line numbers would be incorrect
        with open(self.path, "r") as f:
            for idx, line in enumerate(f):
                stripped = line.strip()
                # Skip empty lines
                if not stripped:
                    continue
                # Check amount of seperators
                parts = stripped.split(self.sep)
                if len(parts) > amount_of_seps + 1:
                    errors.append(
                        f"line: {idx+1} => Line has more than {amount_of_seps} seperator(s) `{self.sep}`"
                    )
                if len(parts) < amount_of_seps + 1:
                    errors.append(
                        f"line: {idx+1} => Line has less than {amount_of_seps} seperator(s) `{self.sep}`"
                    )

        if len(errors) == 0:
            return
        # If there are erros print all of them before exiting
        print(f"{Colour.RED}[ERROR]{Colour.NC} Errorous wordlist:")
        for error in errors:
            print(f"    > {error}")
        exit(f" {Colour.YELLOW}==>{Colour.NC} Too many error exiting")

    # Export keys(questions) and dict(answers from questions)
    def export(self) -> tuple[list[str], dict[str, str]]:
        # Create return value dict
        ret: dict[str, str] = dict()
        p = ClearPrint()
        for idx, text in enumerate(self.contents):
            parts = text.split(self.sep)
            # Check if translator is used
            if self.uses_tl:
                p.print(
                    f"{Colour.GREEN}[{idx+1}/{len(self.contents)}] {Colour.BLUE}Translating {parts[0]} ...{Colour.NC}"
                )
                # Translate word and add it to the dict
                ret[parts[0].strip()] = translate(parts[0].strip(), self.lang).strip()
            else:
                # Add the question and answer to dict
                ret[parts[0].strip()] = parts[1].strip()
        # if --switch swap keys and values
        if self.switch:
            ret = {v: k for k, v in ret.items()}
        # Generate keys
        keys = list(ret.keys())
        # Remove carriage return from translator download
        if self.uses_tl:
            print()
        # Return keys and dict
        return keys, ret
