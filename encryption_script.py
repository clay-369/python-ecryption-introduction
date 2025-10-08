# Importeer encryptiealgoritme Fernet van cryptography
from cryptography.fernet import Fernet

# Importeer de functie om de clipboard te gebruiken
import pyperclip

# Vraag de gebruiker voor een bericht om te versleutelen
message = input("Geef een bericht om te versleutelen: ")

# Key genereren met Fernet voor encryptie
# Er kan ook een andere key generator worden gebruikt!
key = Fernet.generate_key()

# Instantieer de Fernet klasse met de gegenereerde key
fernet_instance = Fernet(key)

# Initialiseer encryptiebericht met None
encrypted_message = None
# Gebruik Fernet klasse instantie om de "message" te encrypten
# De message moet een bytes string zijn voor de encryptie
if message:
    encrypted_message = fernet_instance.encrypt(message.encode())
    if encrypted_message:
        print("Versleutelde bericht is nu gegenereerd!")
else:
    print("Geen bericht ingevoerd!")
    exit()

# Print het versleutelde bericht naar de gebruiker als de gebruiker versleutelde berichten wilt zien
check_encrypted_message = input("Wil je het versleutelde bericht bekijken? (y/n): ")
if check_encrypted_message.lower() == "y":
    print(f"Versleutelde bericht: {encrypted_message}")

# Functionaliteit om het versleutelde bericht naar de clipboard te kopiëren
copy_encrypted_message = input("Wil je het versleutelde bericht kopiëren? (y/n): ")
if copy_encrypted_message.lower() == "y":
    pyperclip.copy(encrypted_message)
    print(f"Versleutelde bericht is nu gekopieerd naar uw clipboard!")

# Gebruik Fernet klasse instantie om het versleutelde bericht te decrypten
check_decrypted_message = input("Wil je het decrypteerde bericht bekijken? (y/n): ")
if check_decrypted_message.lower() == "y":
    decrypted_message = fernet_instance.decrypt(encrypted_message)
    print(f"Decrypteerde bericht: {decrypted_message.decode()}")
    exit()

