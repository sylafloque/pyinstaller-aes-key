# pyinstaller-aes-key

Tout d'abord, générez une clé de chiffrement et enregistrez-la dans un fichier :

```
import os
from cryptography.fernet import Fernet

# Génération d'une clé de chiffrement aléatoire
key = Fernet.generate_key()

# Enregistrement de la clé dans un fichier local
with open('my_key.key', 'wb') as f:
    f.write(key)
```
Ensuite, utilisez PyInstaller pour créer un exécutable à partir de votre script Python

```
pyinstaller --onefile --key=my_key.key my_script.py
```

Après la création de l'exécutable, vous pouvez chiffrer son contenu avec la clé que vous avez générée

```
import base64
from cryptography.fernet import Fernet

# Lecture de l'exécutable chiffré
with open('my_script', 'rb') as f:
    encrypted_data = f.read()

# Lecture de la clé de chiffrement
with open('my_key.key', 'rb') as f:
    key = f.read()

# Déchiffrement de la clé
clear_key = b'qdjFI7_W99jq5zdijsULNH4L1WOJYB9YATsa9ZhcaQU=' # votre clé de chiffrement déchiffrée
fernet = Fernet(clear_key)
decrypted_key = fernet.decrypt(key)

# Déchiffrement de l'exécutable
fernet = Fernet(decrypted_key)
decrypted_data = fernet.decrypt(encrypted_data)

# Écriture de l'exécutable déchiffré dans un fichier
with open('my_script_decrypted', 'wb') as f:
    f.write(decrypted_data)
```
Cet exemple utilise la même méthode de chiffrement que l'exemple 4 précédent, mais il est appliqué à un exécutable PyInstaller plutôt qu'à un simple script Python.
