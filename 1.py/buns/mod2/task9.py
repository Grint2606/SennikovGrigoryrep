string = input()
vowels = sum(1 for char in string if char.lower() in 'aeiouаеёиоуыэюя')
consonants = len(string) - vowels - string.count(' ')
print(f"{vowels} {consonants}")
