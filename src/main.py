# Import modules
import argparse
from parser import File
from util import Lang
from quiz import Quiz


def main():
    # Define cli args
    parser = argparse.ArgumentParser(description="A quizlet clone")
    parser.add_argument("-f", "--file", help="Filepath to wordlist", required=True)
    parser.add_argument(
        "-s",
        "--seperator",
        help="Seperator between question and answer (default '|')",
        default="|",
    )
    parser.add_argument(
        "--switch",
        help="Switch question and answers (default: false)",
        action="store_true",
    )
    parser.add_argument(
        "-t",
        "--translate",
        help="Automatically translate question to generate answer with provided language (default: 'en' to 'de')",
        nargs=2,
        default=None,
        metavar=["FROM", "TO"],
    )
    # Parse arguments
    args = parser.parse_args()
    # Set translation to true if flag was used
    translation_enabled = True if args.translate else False
    # Set translator arg default languages
    translation_defaults = (
        ["en", "de"] if not args.translate else [args.translate[0], args.translate[1]]
    )
    # Create quiz from keys and answers from keys
    Quiz(
        # Create a file from the path and export the keys and answers from keys
        *File(
            args.file,
            args.seperator,
            translation_enabled,
            Lang(*translation_defaults),
            args.switch,
        ).export(),
    ).run()


# Run main
if __name__ == "__main__":
    main()
