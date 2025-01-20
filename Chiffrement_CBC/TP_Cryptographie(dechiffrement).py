import pyfiglet

ascii_banner = pyfiglet.figlet_format("CRYPT-CBC")
print(ascii_banner)

# On demande à l'utilisateur le chemin du fichier que l'on doit récuperer
file_path = input('Mettre le chemin du fichier à déchiffre :')
# On ouvre le fichier que l'utilisateur souhaite
with open(file_path, "rb") as fichier:
    data = fichier.read()

# On ouvre le fichier contenant la cle de chiffrement
with open("cle_chiffrement", "rb") as fichier:
    cle = fichier.read()

# On ouvre le fichier contenant l'iv
with open("iv_chiffrement", "rb") as fichier:
    iv = fichier.read()

# On définit la taille d'un block selon la longueur d'iv
taille_block = len(iv)

# On sépare notre fichier en differents blocks
blocks = [data[i:i + taille_block] for i in range(0, len(data), taille_block)]

# On récupère le premier block
premier_block = blocks[0]

# On définit le resultat du XOR entre le premier résultat du XOR et la clé
xor_dechiffrement_bloc1 = bytes([b ^ cle[i] for i, b in enumerate(premier_block)])

# On définit le résultat du XOR entre le premier block et le iv
xor_dechiffrement_2 = bytes([b ^ iv[i] for i, b in enumerate(xor_dechiffrement_bloc1)])

# On ouvre ensuite un fichier pour recupérer le chiffrement de notre fichier
with open("fichier_dechiffre", "wb") as file:
    file.write(xor_dechiffrement_2)

print("Déchiffrement du fichier en cours ...")

# On creer une boucle pour que chaque blocks qui constitue notre fichier chiffré soit prit en boucle
for i in range(1, len(blocks)):
    block = blocks[i]
    if isinstance(block, str):
        block = block.encode()
    # XOR entre le bloc actuel et le bloc chiffré précédent
    xor_suivant = bytes([b ^ cle[i] for i, b in enumerate(block)])
    xor_final = bytes([x ^ premier_block[i] for i, x in enumerate(xor_suivant)])
    premier_block = block
    with open("fichier_dechiffre", "ab") as file:
        file.write(xor_final)
print("Le fichier a été déchiffré et installé")
