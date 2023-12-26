phone_number = input()
filtered_number = ''.join(char for char in phone_number if char.isdigit() or char == '+')
print(filtered_number)
