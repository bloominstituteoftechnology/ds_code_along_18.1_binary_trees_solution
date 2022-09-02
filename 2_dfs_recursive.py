class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse(root: node):
    values = list()
    traverse_node(root, values)
    return values

def traverse_node(current, values):
    if (current.left is not None):
        traverse_node(current.left, values)
    values.append(current.value)
    if (current.right is not None):
        traverse_node(current.right, values)

# Test cases:
head = node(6)
head.left = node(3)
head.right = node(9)

print(traverse(head)) # 3, 6, 9

# This is the recursive solution. Could also be implemented with an explicitly-declared stack data structure.