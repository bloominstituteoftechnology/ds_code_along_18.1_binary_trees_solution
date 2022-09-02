from collections import deque

class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse(root: node):
    if root is None:
        return
    stack = deque()
    current = root
    values = []

    while (len(stack) > 0 or current is not None):
        if current is not None:
            stack.append(current)
            current = current.left

        else:
            current = stack.pop()
            values.append(current.value)
            current = current.right

    return values

# Test cases:
head = node(6)
head.left = node(3)
head.right = node(9)

print(traverse(head)) # 3, 6, 9

# This is the recursive solution. Could also be implemented with an explicitly-declared stack data structure.