import secrets
import pyfiglet

ascii_banner = pyfiglet.figlet_format("CRYPT-CBC")
print(ascii_banner)

# On demande à l'utilisateur le chemin du fichier que l'on doit récuperer
file_path = input('Mettre le chemin du fichier à chiffre :')
# On ouvre le fichier que l'utilisateur souhaite
with open(file_path, "rb") as file:
    data = file.read()

# On génère un vecteur d'initialisation aléatoire de 16 octets
iv = secrets.token_bytes(16)
# On ouvre un fichier pour y mettre notre Valeur Initiale que l'on doit garder pour le déchiffrement
with open("iv_chiffrement", "wb") as fichier:
    fichier.write(iv)

# On génère la clé aléatoire de 16 octets
cle = secrets.token_bytes(16)
# On ouvre un fichier pour y mettre notre cle que l'on doit garder pour le déchiffrement
with open("cle_chiffrement", "wb")as fichier:
    fichier.write(cle)

# On définit la taille d'un block selon la longueur d'octets de la clé
taille_block = len(cle)

# On sépare notre fichier en differents blocks
blocks = [data[i:i + taille_block] for i in range(0, len(data), taille_block)]

# On récupère le premier block
premier_block = blocks[0]

# On définit le résultat du XOR entre le premier block et le iv
xor_block1 = bytes([b ^ iv[i] for i, b in enumerate(premier_block)])

# On définit le resultat du XOR entre le premier résultat du XOR et la clé
xor_final_block1 = bytes([x ^ cle[i] for i, x in enumerate(xor_block1)])

# On creer ensuite un fichier pour y mettre le chiffrement de notre fichier
with open("fichier_chiffre.txt", "wb") as file:
    file.write(xor_final_block1)

print("Chiffrement du fichier en cours ...")

# On creer une boucle pour que chaque blocks qui constitue notre fichier soit prit en boucle
for i in range(1, len(blocks)):
    block = blocks[i]
    if isinstance(block, str):
        block = block.encode()
    # XOR entre le bloc actuel et le bloc chiffré précédent
    xor_suivant = bytes([b ^ xor_final_block1[i] for i, b in enumerate(block)])
    xor_final_suivant = bytes([x ^ cle[i] for i, x in enumerate(xor_suivant)])
    xor_final_block1 = xor_final_suivant
    with open("fichier_chiffre.txt", "ab") as file:
        file.write(xor_final_suivant)
print("Le fichier a été chiffré et installé")
