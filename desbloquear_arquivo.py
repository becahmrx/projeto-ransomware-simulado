# Aqui iremos descriptografar

import os
import pyaes

# Solicita o nome do arquivo criptografado
file_name = input("Digite o nome do arquivo criptografado (com .ransomwaretroll): ")

# Ler o conteúdo criptografado
with open(file_name, 'rb') as file:
    file_data = file.read()

# Chave de descriptografia (tem que ser igual à usada na criptografia)
key = b'1234567890abcdef'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Salvar o arquivo descriptografado
new_file_name = file_name.replace('.ransomwaretroll', '_decrypted')
with open(new_file_name, 'wb') as new_file:
    new_file.write(decrypt_data)
