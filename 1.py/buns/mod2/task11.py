sequence = list(map(int, input().split()))
result = len(set(sequence)) != len(sequence)
print(result)
