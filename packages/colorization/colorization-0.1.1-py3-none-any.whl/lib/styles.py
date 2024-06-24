@staticmethod
def reset(text):
    return f"\033[0m{text}\033[0m"


@staticmethod
def bold(text):
    return f"\033[1m{text}\033[0m"


@staticmethod
def dim(text):
    return f"\033[2m{text}\033[0m"


@staticmethod
def italic(text):
    return f"\033[3m{text}\033[0m"


@staticmethod
def underline(text):
    return f"\033[4m{text}\033[0m"


@staticmethod
def inverse(text):
    return f"\033[7m{text}\033[0m"


@staticmethod
def hidden(text):
    return f"\033[8m{text}\033[0m"


@staticmethod
def strikethrough(text):
    return f"\033[9m{text}\033[0m"
