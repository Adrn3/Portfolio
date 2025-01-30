# Chiffrement CBC : Programmes de Chiffrement et Déchiffrement de Fichiers

Ce programme permet de **chiffrer** et de **déchiffrer** un fichier en utilisant le mode CBC (**Cipher Block Chaining**).  
Le mode CBC garantit un chiffrement robuste en reliant chaque bloc de données au bloc précédent.  
Le programme génère automatiquement une clé et un vecteur d'initialisation (**IV**) pour assurer la sécurité des données.

---

## 📋 Prérequis

1. **Python 3.x** :  
   Assurez-vous d'avoir Python installé sur votre ordinateur.  
   - **Windows** : Téléchargez Python depuis [python.org](https://www.python.org/).  
   - **Linux** : Installez Python via la commande :  
     ```bash
     sudo apt install python3.10
     ```

2. **Bibliothèques nécessaires** :  
   Ce programme utilise les bibliothèques suivantes :  
   - `pyfiglet` (à installer avec pip)  
   - `secrets` (peut-être inclus nativement dans Python)  

   Installez les bibliothèques manquantes avec :  
   ```bash
   pip install pyfiglet
   pip install secret

## 🚀 Mode d'emploi

Étape 1 : Préparation du fichier
1. Préparation du fichier :
   Placez le fichier que vous souhaitez chiffrer **dans le même dossier que le script Python** .
2. Copiez le chemin complet du fichier pour le coller dans le programme lors de l'exécution.

Étape 2 : Lancer le programme
- **Windows** : 
```bash
   python chiffrement.py

- **Linux** :
```bash
   python3 chiffrement.py

Étape 3 : Fournir le chemin du fichier
Lorsqu'invité par le programme, collez le chemin du fichier précédemment copié.
Suivez les instructions pour finaliser le chiffrement ou le déchiffrement.

##💡 Exemple de sortie

**Clé générée** : Le programme génère une clé aléatoire qui pourrait ressembler à ceci :
b'G5z8K1vP2l0Jm3Nx'
**Vecteur d'initialisation (IV)** : Un IV unique sera également généré, par exemple :
b'9a8b7c6d5e4f3g2h'.

Le fichier chiffré sera enregistré dans le même dossier sous un nouveau nom. Par exemple :
Si le fichier d'origine s'appelle document.txt, le fichier chiffré pourrait s'appeler document_encrypted.txt.

## ❓ Dépannage
**Problèmes fréquents:**
**1. pip non reconnu:**
Vérifiez que Python est bien installé et ajouté à votre PATH (surtout sous Windows).
Consultez ce guide pour plus d'informations : Configurer pip.
**2.Fichier introuvable:**
Assurez-vous que le chemin du fichier est correct et qu'il est dans le même dossier que chiffrement.py.
Vérifiez les permissions d'accès au fichier.
**3.Problèmes liés aux bibliothèques :
Réinstallez les bibliothèques nécessaires avec :
```bash
   pip install pyfiglet

## 📄 Licence
Ce projet est open-source et disponible sous la licence MIT. Vous pouvez l'utiliser, le modifier et le distribuer librement.
