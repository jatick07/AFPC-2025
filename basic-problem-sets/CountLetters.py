def count_letters(string):
    letter_count = {}
    for char in string:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1
            
    return letter_count

user_input = input()
print(count_letters(user_input))