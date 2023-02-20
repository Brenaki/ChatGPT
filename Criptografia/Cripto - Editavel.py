from cryptography.fernet import Fernet

def criptografar(palavra):
    # Gera uma chave aleatória
    key = Fernet.generate_key()
    
    # Cria um objeto Fernet com a chave gerada
    fernet = Fernet(key)
    
    # Converte a palavra em bytes
    palavra_bytes = bytes(palavra, 'utf-8')
    
    # Cifra a palavra
    palavra_cifrada = fernet.encrypt(palavra_bytes)
    
    # Descifra a palavra
    palavra_descifrada = fernet.decrypt(palavra_cifrada)
    
    # Retorna a chave e a palavra cifrada em forma de dicionário
    return {'chave': key, 'palavra_cifrada': palavra_cifrada, 'palavra_descifrada': palavra_descifrada}

palavra = input("Digite a palavra a ser criptografada: ")
resultado = criptografar(palavra)
print("Chave: ", resultado['chave'])
print("Palavra cifrada: ", resultado['palavra_cifrada'])
print("Palavra decifrada: ", resultado['palavra_descifrada'])