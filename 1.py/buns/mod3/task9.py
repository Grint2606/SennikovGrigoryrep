n = int(open('input.txt').read())
x, y = divmod((n - 1) // 2, 4)
print(f"{x - y} {x + 1}")
