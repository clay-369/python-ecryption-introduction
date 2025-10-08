# Importeer encryptiealgoritme Fernet van cryptography
from cryptography.fernet import Fernet

# String die encrypt gaat worden
message = "This is a secret message"

# Key genereren met Fernet voor encryptie
# Er kan ook een andere key generator worden gebruikt!
key = Fernet.generate_key()

# Instantieer de Fernet klasse met de gegenereerde key
fernet_instance = Fernet(key)

# Gebruik Fernet klasse instantie om de "message" te encrypten
# De message moet een bytes string zijn voor de encryptie
encrypted_message = fernet_instance.encrypt(message.encode())

# Print het versleutelde bericht naar de gebruiker
print(f"Versleutelde bericht: {encrypted_message}")

# Gebruik Fernet klasse instantie om het versleutelde bericht te decrypten
decrypted_message = fernet_instance.decrypt(encrypted_message)

# Print het decrypteerde bericht naar de gebruiker
print(f"Decrypteerde bericht: {decrypted_message.decode()}")
