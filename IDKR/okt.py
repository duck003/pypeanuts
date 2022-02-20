from typing import List


class Node:
    def __init__(self, name: int):
        self.name = name
        self.is_root = True
        self.children: List[Node] = []
        self.height = 0


N = int(input())
tree = [Node(i+1) for i in range(N)]

for node in tree:
    children = [int(x)-1 for x in input().split()][1:]
    node.children = [tree[i] for i in children]

for node in tree:
    for child in node.children:
        child.is_root = False

root = None
for node in tree:
    if node.is_root:
        root = node
        break


def calculate_height(node: Node):
    for child in node.children:
        calculate_height(child)
    if node.children:
        node.height = 1 + max([child.height for child in node.children])


calculate_height(root)
print(root.name)
print(sum([node.height for node in tree]))