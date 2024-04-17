n = int(input())
# Upper half of the diamond
spaces = 0
stars = 2 * n  - 1
for i in range(n - 1, 0, -1):
    for j in range(spaces):
        print(" ", end=" ")
    for j in range(stars):
        print("*", end=" ")
    print()
    spaces += 1
    stars -= 2
# Lower half of the diamond
spaces = n-1
stars = 1
for i in range(n):
    for j in range(spaces):
        print(" ", end=" ")
    for j in range(stars):
        print("*", end=" ")
    print()
    spaces -= 1
    stars += 2
