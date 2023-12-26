size = int(input())
matrix = [list(range(1, size + 1))] * size
for row in matrix:
    print(", ".join(map(str, row)))
print()
for row in zip(*matrix):
    print(", ".join(map(str, row)))
