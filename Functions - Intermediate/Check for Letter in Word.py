def check_letter(word, letter):
    return letter in word

print(check_letter("apple", "a"))  # ➞ True
print(check_letter("banana", "z"))  # ➞ False
