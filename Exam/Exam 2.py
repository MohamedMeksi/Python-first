from utils import unzip_with_7z # type: ignore
import itertools
import string

zip_file_path = 'congrats.7z'  # keep as is
dest_path = '.'  # keep as is

# Liste de toutes les lettres minuscules possibles
letters = string.ascii_lowercase  

# Tester toutes les combinaisons de 2 lettres
for combination in itertools.product(letters, repeat=2):
    find_me = ''.join(combination)  # Convertir le tuple en string
    secret_password = find_me + 'bcmpda'  # Construire le mot de passe

    print(f"🔍 Trying password: {secret_password}")

    # Tenter d'ouvrir l'archive avec ce mot de passe
    if unzip_with_7z(zip_file_path, dest_path, secret_password):
        print(f"🎉 Password found: {secret_password}")
        break  # Arrêter le script si le mot de passe est correct
