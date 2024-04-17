n = int(input())
spaces = n - 1
stars = 1
# Upper half of the diamond
for i in range(n):
    for j in range(spaces):
        print(" ", end=" ")
    for j in range(stars):
        print("*", end=" ")
    print()
    spaces -= 1
    stars += 2
# Lower half of the diamond
spaces = 1
stars = 2 * (n - 1) - 1
for i in range(n - 1, 0, -1):
    for j in range(spaces):
        print(" ", end=" ")
    for j in range(stars):
        print("*", end=" ")
    print()
    spaces += 1
    stars -= 2
