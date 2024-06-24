class fg:
    @staticmethod
    def black(text):
        return f"\033[30m{text}\033[0m"

    @staticmethod
    def red(text):
        return f"\033[31m{text}\033[0m"

    @staticmethod
    def green(text):
        return f"\033[32m{text}\033[0m"

    @staticmethod
    def yellow(text):
        return f"\033[33m{text}\033[0m"

    @staticmethod
    def blue(text):
        return f"\033[34m{text}\033[0m"

    @staticmethod
    def magenta(text):
        return f"\033[35m{text}\033[0m"

    @staticmethod
    def cyan(text):
        return f"\033[36m{text}\033[0m"

    @staticmethod
    def white(text):
        return f"\033[37m{text}\033[0m"

    @staticmethod
    def gray(text):
        return f"\033[90m{text}\033[0m"

    @staticmethod
    def grey(text):
        return f"\033[90m{text}\033[0m"

    @staticmethod
    def bright_red(text):
        return f"\033[91m{text}\033[0m"

    @staticmethod
    def bright_green(text):
        return f"\033[92m{text}\033[0m"

    @staticmethod
    def bright_yellow(text):
        return f"\033[93m{text}\033[0m"

    @staticmethod
    def bright_blue(text):
        return f"\033[94m{text}\033[0m"

    @staticmethod
    def bright_magenta(text):
        return f"\033[95m{text}\033[0m"

    @staticmethod
    def bright_cyan(text):
        return f"\033[96m{text}\033[0m"

    @staticmethod
    def bright_white(text):
        return f"\033[97m{text}\033[0m"


class bg:
    @staticmethod
    def black(text):
        return f"\033[40m{text}\033[0m"

    @staticmethod
    def red(text):
        return f"\033[41m{text}\033[0m"

    @staticmethod
    def green(text):
        return f"\033[42m{text}\033[0m"

    @staticmethod
    def yellow(text):
        return f"\033[43m{text}\033[0m"

    @staticmethod
    def blue(text):
        return f"\033[44m{text}\033[0m"

    @staticmethod
    def magenta(text):
        return f"\033[45m{text}\033[0m"

    @staticmethod
    def cyan(text):
        return f"\033[46m{text}\033[0m"

    @staticmethod
    def white(text):
        return f"\033[47m{text}\033[0m"

    @staticmethod
    def gray(text):
        return f"\033[100m{text}\033[0m"

    @staticmethod
    def grey(text):
        return f"\033[100m{text}\033[0m"

    @staticmethod
    def bright_red(text):
        return f"\033[101m{text}\033[0m"

    @staticmethod
    def bright_green(text):
        return f"\033[102m{text}\033[0m"

    @staticmethod
    def bright_yellow(text):
        return f"\033[103m{text}\033[0m"

    @staticmethod
    def bright_blue(text):
        return f"\033[104m{text}\033[0m"

    @staticmethod
    def bright_magenta(text):
        return f"\033[105m{text}\033[0m"

    @staticmethod
    def bright_cyan(text):
        return f"\033[106m{text}\033[0m"

    @staticmethod
    def bright_white(text):
        return f"\033[107m{text}\033[0m"


def random_color(text):
    import random

    color = random.choice([31, 32, 33, 34, 35, 36, 91, 92, 93, 94, 95, 96])
    return f"\033[{color}m{text}\033[0m"
