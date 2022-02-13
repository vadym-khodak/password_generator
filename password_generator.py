import argparse
import math
import random


def generate():
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
    count_chars = args.length
    numbers = []
    if args.numbers:
        numbers = get_numbers(args.length)
    count_chars -= len(numbers)

    special_chars = []
    if args.characters:
        special_chars = get_special_chars(args.length, args.special_characters)
    count_chars -= len(special_chars)

    chars = get_chars(count_chars)

    full_list = chars + numbers + special_chars
    random.shuffle(full_list)
    return "".join(full_list)


def get_chars(count_chars):
    chars = []
    if count_chars <= 52:
        while count_chars > 0:
            random_char = chr(random.choice(list(range(65, 65 + 26)) + list(range(65 + 32, 65 + 32 + 26))))
            if random_char not in chars:
                chars.append(random_char)
                count_chars -= 1
    else:
        for _ in range(count_chars):
            random_char = chr(random.choice(list(range(65, 65 + 26)) + list(range(65 + 32, 65 + 32 + 26))))
            chars.append(random_char)
    return chars


def get_special_chars(length, special_characters):
    special_chars = []
    count_special_characters = math.ceil(length * 10 / 100)
    if count_special_characters <= len(special_characters):
        while count_special_characters > 0:
            random_special_char = random.choice(special_characters)
            if random_special_char not in special_chars:
                special_chars.append(random_special_char)
                count_special_characters -= 1
    else:
        for _ in range(count_special_characters):
            random_special_char = random.choice(special_characters)
            special_chars.append(random_special_char)
    return special_chars


def get_numbers(length):
    numbers = []
    count_nums = math.ceil(length * 10 / 100)
    if count_nums <= 10:
        while count_nums > 0:
            random_num = str(random.randint(0, 9))
            if random_num not in numbers:
                numbers.append(random_num)
                count_nums -= 1
    else:
        for _ in range(count_nums):
            random_num = str(random.randint(0, 9))
            numbers.append(random_num)
    return numbers


if __name__ == "__main__":
    print(generate())
