import argparse

from main import generate_password


def process_cli_command():
    parser = argparse.ArgumentParser(
        description="Password generator is a CLI tool to generate random password."
    )
    parser.add_argument(
        "-l",
        "--length",
        required=False,
        type=int,
        default=8,
        help="Pass length of the password",
    )
    parser.add_argument(
        "-n",
        "--numbers",
        required=False,
        action="store_const",
        const=True,
        default=False,
        help="Pass this flag if you want to include numbers to the password",
    )
    parser.add_argument(
        "-c",
        "--characters",
        required=False,
        action="store_const",
        const=True,
        default=False,
        help="Pass this flag if you want to include special characters to the password",
    )

    parser.add_argument(
        "-s",
        "--special_characters",
        required=False,
        type=str,
        default="-@_.*!",
        help="Pass any special characters you want to use in the password",
    )
    args = parser.parse_args()

    return generate_password(args.length, args.numbers, args.characters, args.special_characters)


if __name__ == "__main__":
    print(process_cli_command())
