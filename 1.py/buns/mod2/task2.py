import math

side_length = int(input())
perimeter = 4 * side_length
area = side_length ** 2
diagonal = round(math.sqrt(2) * side_length, 2)

print(f"{perimeter:.2f}, {area:.2f}, {diagonal:.2f}")
