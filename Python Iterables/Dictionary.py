import string

# 1️⃣ Convertir une liste de tuples en dictionnaire
list_of_tuples = [("name", "Elie"), ("job", "Instructor")]
dictionary = dict(list_of_tuples)
print("1️⃣", dictionary)

# 2️⃣ Convertir deux listes en dictionnaire
states_abbr = ["CA", "NJ", "RI"]
states_names = ["California", "New Jersey", "Rhode Island"]
states_dict = dict(zip(states_abbr, states_names))
print("2️⃣", states_dict)

# 3️⃣ Dictionnaire des voyelles avec valeurs à 0 (sans fromkeys)
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_dict = {vowel: 0 for vowel in vowels}
print("3️⃣", vowel_dict)

# 4️⃣ Dictionnaire des lettres de l’alphabet avec leur position
alphabet_dict = {i + 1: letter for i, letter in enumerate(string.ascii_uppercase)}
print("4️⃣", alphabet_dict)

# 🎖 Super Bonus : Nombre d’occurrences des voyelles dans "awesome sauce"
text = "awesome sauce"
vowel_count = {vowel: text.count(vowel) for vowel in vowels}
print("🎖", vowel_count)
