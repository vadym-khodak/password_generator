import math
import random


def generate_password(
    length: int = 8,
    use_numbers: bool = False,
    use_special_chars: bool = False,
    special_characters: str = "-@_.*!",
) -> str:
    count_chars = length
    numbers = []
    if use_numbers:
        numbers = get_numbers(length)
    count_chars -= len(numbers)
    special_chars = []
    if use_special_chars:
        special_chars = get_special_chars(length, special_characters)
    count_chars -= len(special_chars)
    chars = get_chars(count_chars)
    full_list = chars + numbers + special_chars
    random.shuffle(full_list)
    return "".join(full_list)


def get_chars(count_chars: int) -> list[str]:
    chars = []
    if count_chars <= 52:
        while count_chars > 0:
            random_char = chr(
                random.choice(
                    list(range(65, 65 + 26)) + list(range(65 + 32, 65 + 32 + 26))
                )
            )
            if random_char not in chars:
                chars.append(random_char)
                count_chars -= 1
    else:
        for _ in range(count_chars):
            random_char = chr(
                random.choice(
                    list(range(65, 65 + 26)) + list(range(65 + 32, 65 + 32 + 26))
                )
            )
            chars.append(random_char)
    return chars


def get_special_chars(length: int, special_characters: str) -> list[str]:
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


def get_numbers(length: int) -> list[str]:
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
