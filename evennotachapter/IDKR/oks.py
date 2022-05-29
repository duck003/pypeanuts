s1 = input().split()
s2 = []

while s1:
    c = s1.pop()
    if c == "f":
        x = s2.pop()
        s2.append(2*x - 3)
    elif c == "g":
        x = s2.pop()
        y = s2.pop()
        s2.append(2*x + y - 7)
    elif c == "h":
        x = s2.pop()
        y = s2.pop()
        z = s2.pop()
        s2.append(3*x - 2*y + z)
    else:
        s2.append(int())

print(*s2)