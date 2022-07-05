# ===== Module & Library
import random
import string

# ===== Header
LIST_NUMBERS = "0123456789"
LIST_CHARS = string.ascii_letters

# ===== Function

# ===== Class

# ===== Main
def RandomNumber(length=6):
    """Function to generate random number"""

    numbers = "".join(random.choice(LIST_NUMBERS) for i in range(length))
    return numbers


def RandomString(length=6):
    """Function to generate random string"""

    strings = "".join(random.choice(LIST_CHARS) for i in range(length))
    return strings
