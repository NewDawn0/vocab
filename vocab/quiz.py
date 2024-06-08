from random import shuffle
from .util import Colour
from difflib import SequenceMatcher


class Quiz:
    def __init__(self, to_learn: list[str], answers: dict[str, str]) -> None:
        self.to_learn = to_learn
        self.answers = answers
        self.total = len(to_learn)
        self.learned: list[str] = list()
        self.prev_word = ""

    def _ask(self) -> None:
        # Shuffle until previous word is not new word
        if len(self.to_learn) > 2:
            while True:
                shuffle(self.to_learn)
                if self.to_learn[0] != self.prev_word:
                    break
        # Shuffle once
        else:
            shuffle(self.to_learn)
        word = self.to_learn[0]
        self.prev_word = self.to_learn[0]

        # Get user input
        user_answer = input(
            f"\n{Colour.GREEN}[{len(self.learned)}/{self.total}]{Colour.NC} Enter word(s) for `{Colour.BLUE}{word}{Colour.NC}`: "
        )
        # Get anwer
        answer = self.answers[word]
        # If correct answer
        if user_answer == answer:
            self.learned.append(word)
            del self.to_learn[0]
            print(f"{Colour.GREEN}Correct 👍{Colour.NC}")
        # Wrong answer
        else:
            out, hint = self._show_diff(user_answer, self.answers[word])
            print(f"{out}\n{hint}")

    @staticmethod
    def _show_diff(question: str, answer: str) -> tuple[str, str]:
        seqm = SequenceMatcher(None, question, answer)
        output = []
        hint = []
        for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
            match opcode:
                case "equal":
                    output.append(seqm.a[a0:a1])
                    hint.append(" " * len(seqm.a[a0:a1]))
                case "insert":
                    output.append(f"{Colour.GREEN}{seqm.b[b0:b1]}{Colour.NC}")
                    hint.append(f"{Colour.GREEN}+{Colour.NC}" * len(seqm.b[b0:b1]))
                case "delete":
                    rm_text = "".join(c + "\u0336" for c in seqm.a[a0:a1])
                    output.append(f"{Colour.RED}{rm_text}{Colour.NC}")
                    hint.append(f"{Colour.RED}-{Colour.NC}" * len(seqm.a[a0:a1]))
                case "replace":
                    output.append(f"{Colour.YELLOW}{seqm.b[b0:b1]}{Colour.NC}")
                    hint.append(f"{Colour.YELLOW}^{Colour.NC}" * len(seqm.b[b0:b1]))
        return "".join(output), "".join(hint)

    def run(self) -> None:
        # Run util no more words left to learn
        while len(self.to_learn) > 0:
            self._ask()
        print(f"{Colour.BLUE}You've learned everything 🏆{Colour.NC}")
