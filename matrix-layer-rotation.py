def defLayer(m, n, i, j):
    return min(i, j, m-i-1, n-j-1)

def rotate(i, j, l, x, y, r, m, n):

    # Calculate layer size
    width = n - 2 * l
    height = m - 2 * l
    size = 2 * (width + height) - 4
    r = r % size

    # Calculate layer
    # z, w = rotate2(i, j, l, x, y, r)
    while (r > 0):
        # Top Left 
        if i == l and j == l:
            if r >= height - 1:
                i, j = x - 1, l
                r = r - height + 2
            else:
                i, j = l+1, l 
        # Top Right
        elif i == l and j == y-1:
            if r >= width - 1:
                i, j = l, l
                r = r - width + 2
            else:
                i, j = l, y-2
        # Bottom Right
        elif i == x-1 and j == y-1:
            i, j = x-2, y-1
        # Bottom Left
        elif i == x-1 and j == l:
            i, j = x-1, l+1
        # Top
        elif i == l:
            i, j = i, j-1 
        # Right
        elif j == y-1:
            i, j = i-1, j
        # Bottom
        elif i == x-1:
            i, j = x-1, j+1
        # Left
        elif j == l:
            i, j = i+1, j
        r = r-1

    return (i, j)

mnr = input().split()
m = int(mnr[0])
n = int(mnr[1])
r = int(mnr[2])

a = [[0 for x in range(n)] for y in range(m)] 
for i in range(0, m):
    line = list(map(int, list(input().rstrip().split())))
    for j in range(0, n):
        l = defLayer(m, n, i, j)
        z, w = rotate(i, j, l, m-l, n-l, r, m, n)
        a[z][w] = line[j]

for i in a:
    print(' '.join(list(map(str, i))))
