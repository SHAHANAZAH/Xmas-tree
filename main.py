width = 5
height = 4

space = width * height
n = 1
width =5
height =4

space = width * height
n = 1
print(('MERRY CHRISTMAS').center(30))

for x in range(1, height + 1):
    for i in range(n, width + 1):
        for j in range(space, i - 1, -1):
            print(end = ' ')
        for k in range(1, i + 1):
            print('@', end = ' ')
        print()
    n = n + 2
    width = width + 2

for i in range(1, height):
    for j in range(space - 3, -1, -1):
        print(end = ' ')
    for k in range(1, height):
        print('@', end = ' ')
    print()

for x in range(1, height + 1):
    for i in range(n, width + 1):
        for j in range(space, i - 1, -1):
            print(end = ' ')
        for k in range(1, i + 1):
            print('@', end = ' ')
        print()
    n = n + 2
    width = width + 2

for i in range(1, height):
    for j in range(space - 3, -1, -1):
        print(end = ' ')
    for k in range(1, height):
        print('@', end = ' ')
    print()
