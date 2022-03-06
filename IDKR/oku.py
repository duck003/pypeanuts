from typing import List
z = int(input()) 


class Node():

    def __init__(self, name):
        self.name = name
        self.is_root = True
        self.children:List[Node] = []
        self.height = 0
        self.is_visited = False
    

tree:List[Node] = []

for i in range(z):
    tree.append(Node(i+1))

for i in range(z):
    a = [int(x) for x in input().split()]
    if a[0] != 0:
        a = a[1:]
        for j in range(len(a)):
           tree[i].children.append(tree[a[j]-1])

for node in tree:
    for child in node.children:
        child.is_root = False

root = None
for node in tree: 
    if node.is_root:
        root = node
        print(root.name)
         
    
def cal(node:Node):
    st = [root]
    while st:
        c = st[-1]
        if c.is_visited == True:
            st.pop()
            if c.children:
                c.height = 1+max([child.height for child in c.children])
        else:
            for child in c.children:
                st.append(child)
            c.is_visited = True
                    
cal(root)
print(sum([node.height for node in tree]))