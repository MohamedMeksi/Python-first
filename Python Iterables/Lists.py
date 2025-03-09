# 1. Print all values in the list one by one.
lst = [1, 2, 3, 4]
for num in lst:
    print(num)

# 2. Print all values in the list multiplied by 20.
multiplied_lst = [num * 20 for num in lst]
print(multiplied_lst)  # Output: [20, 40, 60, 80]

# 3. Return a new list with only the first letter of each name.
names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in names]
print(first_letters)  # Output: ["E", "T", "M"]

# 4. Return a new list with all even values.
nums = [1, 2, 3, 4, 5, 6]
evens = [num for num in nums if num % 2 == 0]
print(evens)  # Output: [2, 4, 6]

# 5. Return a new list that contains only the values present in both lists.
lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
common_values = [num for num in lst1 if num in lst2]
print(common_values)  # Output: [3, 4]

# 6. Return a new list with each word reversed and in lowercase.
words = ["Elie", "Tim", "Matt"]
reversed_words = [word[::-1].lower() for word in words]
print(reversed_words)  # Output: ["eile", "mit", "ttam"]

# 7. Return a new list of the letters present in both strings.
str1 = "first"
str2 = "third"
common_letters = [char for char in str1 if char in str2]
print(list(set(common_letters)))  # Output: ["i", "r", "t"]

# 8. Return a list of numbers between 1 and 100 that are divisible by 12.
div_by_12 = [num for num in range(1, 101) if num % 12 == 0]
print(div_by_12)  # Output: [12, 24, 36, 48, 60, 72, 84, 96]

# 9. Remove all vowels from the string "amazing".
vowels = "aeiou"
word = "amazing"
no_vowels = [char for char in word if char not in vowels]
print(no_vowels)  # Output: ["m", "z", "n", "g"]

# 10. Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
nested_list = [[0, 1, 2] for _ in range(3)]
print(nested_list)  # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# 11. Generate a list with the given structure.
big_nested_list = [[i for i in range(10)] for _ in range(10)]
print(big_nested_list)
