number = int(input())
if number <= 0:
    print("Неверный ввод")
else:
    binary_code = bin(number)[2:]
    octal_code = oct(number)[2:]
    hex_code = hex(number)[2:]
    print(f"{binary_code}, {octal_code}, {hex_code}")
