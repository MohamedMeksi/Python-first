# 1. Declare a variable called first and assign it to "Hello World".
first = "Hello World"

# 2. Write a comment that says "This is a comment."
# This is a comment.

# 3. Log a message to the terminal that says "I AM A COMPUTER!"
print("I AM A COMPUTER!")

# 4. Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2.
if 1 < 2 and 4 > 2:
    print("Math is fun.")

# 5. Assign a variable called nope to an absence of value.
nope = None  # None représente une absence de valeur en Python.

# 6. Use the "and" boolean operator to combine True and False.
result = True and False  # Résultat: False

# 7. Calculate the length of the string "What's my length?"
length = len("What's my length?")

# 8. Convert the string "i am shouting" to uppercase.
shouting = "i am shouting".upper()

# 9. Convert the string "1000" to the number 1000.
num = int("1000")

# 10. Combine the number 4 with the string "real" to produce "4real".
combo = str(4) + "real"

# 11. Record the output of the expression 3 * "cool".
repeat_string = 3 * "cool"  # Résultat: "coolcoolcool"

# 12. Record the output of the expression 1 / 0.
# ⚠️ Attention: Cela va provoquer une erreur "ZeroDivisionError"
# result_error = 1 / 0 

# 13. Determine the type of [].
list_type = type([])  # Résultat: <class 'list'>

# 14. Ask the user for their name and store it in a variable called name.
name = input("What is your name? ")

# 15. Ask the user for a number and check its sign.
number = int(input("Enter a number: "))
if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

# 16. Find the index of "l" in "apple".
index_l = "apple".index("l")  # Résultat: 3

# 17. Check whether "y" is in "xylophone".
is_y_in_xylophone = "y" in "xylophone"  # Résultat: True

# 18. Check whether a string called my_string is all in lowercase.
my_string = "hello"
is_lowercase = my_string.islower()  # Résultat: True
