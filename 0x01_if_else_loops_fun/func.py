def islower(c):
    """Function checks for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


def isupper(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return True
    else:
        return False


islower("r")
islower("R")
isupper("R")
isupper("r")
