import heapq


class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def create_tree(alpha, freq):
    def print_tree(node, level=0):
        if node is None:
            return

        # print right side first (so it appears on top)
        print_tree(node.right, level + 1)

        # print current node
        print("   " * level + str(node.freq) + (f" ({node.char})" if node.char else ""))

        # print left side
        print_tree(node.left, level + 1)
    prio = []

    for i in range(len(alpha)):
        node = Node(alpha[i], freq[i])
        heapq.heappush(prio, node)

    while len(prio) > 1:
        left = heapq.heappop(prio)
        right = heapq.heappop(prio)

        new_node = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(prio, new_node)

        print("\nAfter merge:")
        print_tree(new_node)

    return heapq.heappop(prio)


def is_leaf(node):
    return node.left is None and node.right is None


def decode(stream, huffman):
    output = ""
    current = huffman

    for b in stream:
        if b == 0:
            current = current.left
        else:
            current = current.right

        if is_leaf(current):
            output += current.char
            current = huffman

    if current != huffman:
        raise ValueError("Corrupted encoding")

    return output


def print_codes(node, code=""):
    if node is None:
        return

    if is_leaf(node):
        print(node.char, "=", code)
        return

    print_codes(node.left, code + "0")
    print_codes(node.right, code + "1")

def build_map(node, route, code):
    if is_leaf(node):
        code[node.char] = route
    else:
        build_map(node.left, route + '0', code)
        build_map(node.right, route + '1', code)


def create_map(tree):
    code = {}
    build_map(tree, "", code)
    return code

alpha = ['A', 'B', 'C', 'D']
freq = [5, 9, 12, 13]

root = create_tree(alpha, freq)

print_codes(root)

decoded = decode([0, 0, 0, 1, 1, 0, 1, 1], root)
print("Decoded:", decoded)