def euclidean_algorithm(a, b):
    if b == 0:
        return a
    else:
        return алгоритм евклида(b, a % b)
