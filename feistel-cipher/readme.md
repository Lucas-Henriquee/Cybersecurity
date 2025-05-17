# 🔐 Cifra de Feistel - Ferramenta Interativa

Este projeto implementa uma **Cifra de Feistel com 16 rodadas**, utilizando operações reversíveis como XOR e uma variante simples com S-Box inspirada no DES. A ferramenta permite a encriptação e desencriptação de mensagens de forma segura e didática.

---

## 🧠 O que é a Cifra de Feistel?

A **Cifra de Feistel** é uma estrutura de cifra amplamente utilizada em criptografia simétrica, incluindo algoritmos famosos como o DES. Ela divide os dados em duas metades e aplica uma série de rodadas que combinam substituição e permutação de forma reversível.

Características principais:

- Estrutura simétrica: mesma lógica para encriptação e desencriptação.
- Operações reversíveis (XOR).
- Suporte a funções complexas como S-Box.
- Robustez contra ataques, mesmo com operações simples.

---

## 📁 Estrutura do Projeto

| Arquivo              | Função                                                                 |
|----------------------|------------------------------------------------------------------------|
| `main.py`            | Interface interativa com o usuário para encriptar e desencriptar texto |
| `cipher_engine.py`   | Converte texto em binário, aplica a cifra de Feistel e reverte o binário |
| `feistel_rounds.py`  | Implementa a lógica das rodadas, XOR, função f e substituição via S-Box |
| `sample_text.py`     | Fornece texto de exemplo padrão para testes                            |
| `util.py`            | Funções auxiliares de interface                                        |

---

## 🧪 Como Utilizar

1. **Execute o programa principal:**

```bash
python main.py
```

2. **Escolha uma das opções do menu:**

- Encriptar texto de exemplo
- Encriptar seu próprio texto
- Desencriptar seu próprio texto

3. **Visualize os resultados da cifra.**

- A chave de 16 rodadas é gerada automaticamente a partir de um seed fixo.
- A desencriptação só funciona corretamente com a mesma chave da encriptação.
- O resultado da cifra é exibido em formato **Base64** apenas para facilitar a cópia e transporte seguro do texto cifrado.

---

## 🔧 Detalhes Técnicos

- Número de rodadas: 16
- Tamanho do bloco: 16 bits (8 bits para cada lado)
- Chave: 16 subchaves geradas pseudoaleatoriamente de 8 bits
- Função f:
  - Utiliza XOR e uma mini S-Box de 4 bits, inspirada na S-Box do DES (apenas como substituição simples)
- Operações usadas: XOR, divisão de blocos, substituição

---

## 🔁 Reversibilidade

A estrutura de Feistel garante que a desencriptação possa ser feita aplicando as mesmas rodadas em ordem reversa, sem necessidade de inverter a lógica interna da função.

---

## 🔐 Exemplo de Execução

```plaintext
=== Feistel Cipher Tool ===
1. Encrypt the default sample text
2. Encrypt your own text
3. Decrypt your own text
0. Exit

Enter your text: IMPORTANT SECRET

=== Encryption Result ===
Encrypted (Base64):  g0hVqg8miklCAVGnHu0f5A==

=== Decryption Result ===
Decrypted: IMPORTANT SECRET
```

---

## 🧠 Conceitos Envolvidos

- **Criptografia Simétrica**: mesma chave é usada para encriptar e desencriptar.
- **Cifras em Bloco**: os dados são divididos em blocos binários de tamanho fixo.
- **XOR**: operação lógica reversível ideal para cifras.
- **S-Box**: substituição não-linear que aumenta a confusão da cifra.
- **Rodadas Feistel**: transforma qualquer função f em uma cifra reversível.

---

## 📚 Referências

- [Nature - Feistel Ciphers](https://www.nature.com/articles/s41598-023-47607-6)
- [Wikipedia - DES Supplementary Material](https://en.wikipedia.org/wiki/DES_supplementary_material)

---