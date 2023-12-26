def is_palindrome(word):
    return word == word[::-1]

def make_palindrome(word):
    if is_palindrome(word):
        return word
    else:
        return word + word[-2::-1]


залача 5
def count_letters(file_name):
    stats = {}
    with open(file_name, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    char_lower = char.lower()
                    stats[char_lower] = stats.get(char_lower, 0) + 1

    sorted_stats = dict(sorted(stats.items(), key=lambda item: item[1]))

    with open('folder.txt', 'w') as result_file:
        for char, count in sorted_stats.items():
            result_file.write(f"{char}: {count}\n")
