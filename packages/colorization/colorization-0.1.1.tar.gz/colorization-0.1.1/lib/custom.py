import random
import time


def rainbow(text):
    colors = [31, 33, 32, 36, 34, 35]
    colored_text = "".join(
        f"\033[{color}m{char}" for color, char in zip(colors * len(text), text)
    )
    return f"{colored_text}\033[0m"


def zebra(text):
    colors = [37, 30]
    colored_text = "".join(
        f"\033[{colors[i % 2]}m{char}" for i, char in enumerate(text)
    )
    return f"{colored_text}\033[0m"


def trap(text):
    normal_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    upside_down_chars = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    result = []
    for char in text:
        if char in normal_chars:
            index = normal_chars.index(char)
            trap_char = upside_down_chars[index]
            result.append(trap_char)
        else:
            result.append(char)

    return "".join(result)


def freaky(text):
    char_map = {
        "a": "𝓪",
        "b": "𝓫",
        "c": "𝓬",
        "d": "𝓭",
        "e": "𝓮",
        "f": "𝓯",
        "g": "𝓰",
        "h": "𝓱",
        "i": "𝓲",
        "j": "𝓳",
        "k": "𝓴",
        "l": "𝓵",
        "m": "𝓶",
        "n": "𝓷",
        "o": "𝓸",
        "p": "𝓹",
        "q": "𝓺",
        "r": "𝓻",
        "s": "𝓼",
        "t": "𝓽",
        "u": "𝓾",
        "v": "𝓿",
        "w": "𝔀",
        "x": "𝔁",
        "y": "𝔂",
        "z": "𝔃",
        "A": "𝓐",
        "B": "𝓑",
        "C": "𝓒",
        "D": "𝓓",
        "E": "𝓔",
        "F": "𝓕",
        "G": "𝓖",
        "H": "𝓗",
        "I": "𝓘",
        "J": "𝓙",
        "K": "𝓚",
        "L": "𝓛",
        "M": "𝓜",
        "N": "𝓝",
        "O": "𝓞",
        "P": "𝓟",
        "Q": "𝓠",
        "R": "𝓡",
        "S": "𝓢",
        "T": "𝓣",
        "U": "𝓤",
        "V": "𝓥",
        "W": "𝓦",
        "X": "𝓧",
        "Y": "𝓨",
        "Z": "𝓩",
    }

    freaky_text = ""
    for char in text:
        if char in char_map:
            freaky_text += char_map[char]
        else:
            freaky_text += char

    # get more freaky :3
    emojis = [" 👅", " 🫦", " 😍"]
    random_emoji = random.choice(emojis)
    freaky_text += random_emoji

    return freaky_text
