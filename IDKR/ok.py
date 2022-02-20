z = int(input())
nfile = []
ffile = []

for i in range(z):
    a = [int(x) for x in input().split()]
    nfile.append(a)


def get_first(file):
    return file[0]

sfile  = sorted(nfile, key = get_first)


a , b = sfile[0]

for i in range(1, len(nfile)):
    c , d = sfile[i]
    if c > b :
        ffile.append([a,b])
        a , b = c , d
    elif b < d:
        b = d
ffile.append([a,b])

x = sum ([b-a for a , b in ffile])

print(x)
         