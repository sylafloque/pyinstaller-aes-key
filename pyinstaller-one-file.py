import base64
from cryptography.fernet import Fernet
import PyInstaller.__main__


# Générer une nouvelle clé Fernet et l'enregistrer dans un fichier
key = Fernet.generate_key()
with open('encryption_key.txt', 'wb') as f:
    f.write(key)

# Charger la clé de chiffrement Fernet à partir d'un fichier
with open('encryption_key.txt', 'rb') as f:
    key = f.read()

# Générer un objet Fernet à partir de la clé chargée
fernet = Fernet(key)

# Compiler le script Python en un exécutable
PyInstaller.__main__.run([
    '--name=mon_script',
    '--onefile',
    '--key={}'.format(base64.b64encode(key).decode('utf-8')),
    'mon_script.py'
])
# Notez que nous avons ajouté une étape pour encoder la clé en base64 avant de la passer à PyInstaller en tant qu'argument de la ligne de commande. Cela ajoute une couche de sécurité supplémentaire en évitant de stocker la clé en texte brut dans le code ou sur le disque.
