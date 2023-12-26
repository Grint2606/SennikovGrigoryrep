char, n = input().split()
n = int(n)
result = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
print(result)
