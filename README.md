# 🔐 Projeto: Ransomware Simulado

Este projeto é uma simulação educacional de como funciona a criptografia e descriptografia de arquivos usando Python. O objetivo é entender como proteger arquivos com uma chave e depois restaurá-los, como parte de um exercício prático.

## 📁 Arquivos do Projeto

- `arquivo_cadeado.py`: Script responsável por criptografar um arquivo.
- `desbloquear_arquivo.py`: Script responsável por descriptografar o arquivo criptografado.

## 🧠 Como Funciona

1. Um arquivo é escolhido para ser criptografado (ex: `atestado.docx`).
2. O conteúdo é lido em modo binário.
3. O conteúdo é criptografado com a biblioteca `pyaes` e salvo com uma nova extensão `.ransomwaretroll`.
4. O arquivo original é removido.
5. Para restaurar, o script de descriptografia reverte o processo e gera um novo arquivo com sufixo `_decrypted`.

---

## ▶️ Como Usar

### 🔐 Criptografar um arquivo

1. Coloque o arquivo que deseja criptografar na mesma pasta dos scripts.
2. Abra o terminal (Git Bash ou VSCode) e navegue até essa pasta.
3. Execute o script:

```bash
python arquivo_cadeado.py
```

Isso fará o seguinte:

- O arquivo original será lido e criptografado.
- Um novo arquivo será criado com a extensão `.ransomwaretroll`.
- O arquivo original será excluído automaticamente.

### 🔓 Descriptografar um arquivo

4. Execute o script de descriptografia:

```bash
python desbloquear_arquivo.py
```

Isso fará o seguinte:

- O conteúdo será restaurado para um novo arquivo.
- O novo arquivo terá o sufixo `_decrypted` no nome.

---

## 💡 Melhorias Futuras

- Ocultar a chave de criptografia em um local seguro
- Adicionar senha para descriptografar
- Interface gráfica para facilitar o uso
- Criptografar múltiplos arquivos em lote

## 🧾 Licença

Este projeto é apenas para fins educacionais.
