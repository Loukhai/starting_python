def islower(c):
    """Function checks for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


islower("r")
islower("R")


def isupper(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return True
    else:
        return False


isupper("R")
isupper("r")


def print_last_digit(number):
    print(abs(number) % 10, end="")
    return abs(number) % 10


print_last_digit(109)


def remove_char_at(str, n):
    if n < 0:
        return str
    return str[:n] + str[n + 1 :]


remove_char_at("rabia", 2)
