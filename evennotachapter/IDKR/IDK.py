from typing import List
N = int(input())

class Node:
    def __init__(self, name):
        self.name = name
        self.is_root = True
        self.parent = None
        self.children: List[Node] = []
        self.is_visited = False
        self.depth = 0

tree = [Node(i) for i in range(N)]

for _ in range(N-1):
    i,j = map(int, input().split())
    tree[i].children.append(tree[j])
    tree[j].parent = tree[i]

def dfs(node: Node):
    neighbor = node.children
    if node.parent:
        neighbor.append(node.parent)
    node.is_visited = True
    for n in neighbor:
        if not n.is_visited:
            n.depth = node.depth+1
            dfs(n)

for n in tree:
    for c in n.children:
        c.is_root = False

for node in tree:
    if node.is_root:
        dfs(node)
        
deepest = max(tree, key=lambda n:n.depth)