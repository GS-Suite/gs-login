import random
import string
import re


async def id_generator(class_name, created_time):
    size = 7
    charSet = string.ascii_lowercase + string.ascii_uppercase + \
        string.digits + class_name + created_time
    charSet = re.sub(r"\s+", "", charSet)
    charSet = charSet.strip()
    return ''.join(random.choice(charSet) for _ in range(size))
