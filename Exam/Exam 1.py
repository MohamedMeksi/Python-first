import random

def number_guessing_game():
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    # Générer un nombre aléatoire entre 1 et 100
    random_number = random.randint(1, 100)
    max_attempts = 7  # Nombre maximum d'essais

    for attempt in range(1, max_attempts + 1):
        # Demander à l'utilisateur de deviner
        guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess ➜ "))

        # Vérifier la réponse
        if guess < random_number:
            print("❌ Too low! Try again.")
        elif guess > random_number:
            print("❌ Too high! Try again.")
        else:
            print(f"🎉 Correct! The number was {random_number}. You guessed it in {attempt} attempts.")
            break  # Sortie du jeu si la réponse est correcte
    else:
        # Si l'utilisateur n'a pas trouvé le nombre après max_attempts essais
        print(f"💀 Game Over! The correct number was {random_number}.")

# Exécuter le jeu
number_guessing_game()
