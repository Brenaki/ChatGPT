from cryptography.fernet import Fernet

# Gera uma chave aleatória
key = Fernet.generate_key()

# Cria um objeto Fernet com a chave gerada
fernet = Fernet(key)

# Define um texto a ser cifrado
texto_original = b'teste'

# Cifra o texto
texto_cifrado = fernet.encrypt(texto_original)

# Decifra o texto
texto_decifrado = fernet.decrypt(texto_cifrado)

# Imprime o texto original, o texto cifrado e o texto decifrado
print("Texto original: ", texto_original)
print("Texto cifrado: ", texto_cifrado)
print("Texto decifrado: ", texto_decifrado)
