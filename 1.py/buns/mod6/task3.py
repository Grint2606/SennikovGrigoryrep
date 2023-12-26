def armstrongNumbers():
    n = 10  # Числа 0-9 не учитывать.
    while 1:
        digits = [int(digit) for digit in str(n)]
        power = len(digits)
        if n == sum(digit ** power for digit in digits):
            yield n
        n += 1
