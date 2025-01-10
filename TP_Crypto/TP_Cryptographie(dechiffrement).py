import string
import secrets
import os
import mmap
import time

def CBC_dechiffrement():
    start_time = time.perf_counter()
    with open("fichier_chiffre.txt", "rb") as fichier:
        data = fichier.read()
    #print(data)
    with open("cle_chiffrement", "rb") as fichier:
        cle = fichier.read()
    #print(cle)
    with open("iv_chiffrement", "rb") as fichier:
        iv = fichier.read()
    #print(iv)
    taille_block = len(iv)
    blocks = [data[i:i + taille_block] for i in range(0, len(data), taille_block)]
    #print(blocks)
    premier_block = blocks[0]
    xor_dechiffrement_bloc1 = bytes([b ^ cle[i] for i, b in enumerate(premier_block)])
    #print(xor_dechiffrement_bloc1)
    xor_dechiffrement_2 = bytes([b ^ iv[i] for i, b in enumerate(xor_dechiffrement_bloc1)])
    #print(xor_dechiffrement_2)
    
    with open("fichier_dechiffre", "wb") as file:
        file.write(xor_dechiffrement_2)
    
    for i in range(1, len(blocks)):
        block = blocks[i]
        if isinstance(block, str):
            block = block.encode()
        # XOR entre le bloc actuel et le bloc chiffré précédent
        xor_suivant = bytes([b ^ cle[i] for i, b in enumerate(block)])
        xor_final = bytes([x ^ premier_block[i] for i, x in enumerate(xor_suivant)])
        premier_block = block
        #print(xor_final)
        with open("fichier_dechiffre", "ab") as file:
            file.write(xor_final)
            
    end_time = time.perf_counter()
    execute_time = (end_time - start_time) * 1000000
    print(f"Execution time : {round(execute_time, 6)}")
    #execute_time = end_time - start_time
    #print(execute_time)