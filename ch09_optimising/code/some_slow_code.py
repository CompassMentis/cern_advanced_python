"To profile: python -m cProfile some_slow_code.py"
import random
import string
import time

STRING_LENGTH = 100
NUMBER_OF_STRINGS = 1_000
RANDOM_STRINGS = [
    ''.join(random.choice(string.ascii_letters) for _ in range(STRING_LENGTH))
    for _ in range(NUMBER_OF_STRINGS)
    ]


def version_functional_programming():
    def replace_one(lines):
        if lines:
            return lines[0].replace('a', 'A') + replace_one(lines[1:])
        else:
            return ''
    chunk_size = 100
    chunks = []
    for start in range(0, len(RANDOM_STRINGS), chunk_size):
        time.sleep(0.1)
        chunks.append(
            replace_one(RANDOM_STRINGS[start:start+chunk_size])
        )
    return ''.join(chunks)


print(len(version_functional_programming()))
# Output: 100000
