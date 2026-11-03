"""Check bracket balance using a stack."""

from queue_two_stacks import Stack

OPEN_TO_CLOSE = {"(": ")", "[": "]", "{": "}"}
CLOSING = set(OPEN_TO_CLOSE.values())


def is_balanced(text):
    """Return True if brackets in text are properly nested and matched."""
    stack = Stack()
    for char in text:
        if char in OPEN_TO_CLOSE:
            stack.push(char)
        elif char in CLOSING:
            if len(stack) == 0:
                return False
            if OPEN_TO_CLOSE[stack.pop()] != char:
                return False
    return len(stack) == 0
