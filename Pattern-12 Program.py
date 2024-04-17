n = int(input())
spaces = 0
stars = 2 * n  - 1
for i in range(n - 1, -1, -1):
    for j in range(spaces):
        print(" ", end=" ")
    for j in range(stars):
        print(j+1, end=" ")
    print()
    spaces += 1
    stars -= 2
