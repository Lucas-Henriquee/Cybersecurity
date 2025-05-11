# 🔐 Cifra de César - Ferramenta Interativa

Este projeto implementa uma ferramenta interativa para encriptação e desencriptação de mensagens utilizando a **Cifra de César**, uma das cifras de substituição mais antigas da criptografia clássica.

## 🧠 O que é a Cifra de César?

A **Cifra de César** é uma técnica de **criptografia simétrica por substituição monoalfabética**. Ela consiste em substituir cada letra da mensagem original por outra letra do alfabeto, deslocada por um valor fixo (chave `k`).  
Por exemplo, com um deslocamento de `k = 3`:
- A → D  
- B → E  
- C → F  
- ...

É considerada uma cifra simples, porém útil para introduzir os conceitos básicos de criptografia como chave, cifra, criptograma, encriptação e criptoanálise.

---

## 📁 Estrutura do Projeto

| Arquivo            | Função                                                                 |
|--------------------|------------------------------------------------------------------------|
| `main.py`          | Interface principal com o usuário para encriptar ou desencriptar texto |
| `encrypt.py`       | Implementa as funções de encriptação e desencriptação                  |
| `analysis.py`      | Realiza análise de frequência das letras                               |
| `sample_text.py`   | Fornece um texto de exemplo padrão para testes                         |
| `util.py`          | Funções auxiliares de interface            |

---

## 🧪 Como Utilizar

1. **Execute o programa principal:**

```bash
python main.py
```

2. **Escolha uma das opções do menu:**
- Encriptar texto de exemplo
- Encriptar seu próprio texto
- Desencriptar um texto cifrado

3. **Informe o valor da chave (deslocamento) desejado.**

4. **Visualize o resultado da cifra, e se quiser, analise a frequência das letras.**

---

## 🔎 Análise de Frequência

A ferramenta permite verificar a frequência das letras no texto cifrado, útil para ilustrar **ataques por força bruta** e conceitos de **criptoanálise**.

📊 A análise de frequência pode ajudar a:
- Quebrar a cifra com base nas letras mais comuns
- Entender por que cifras simples são vulneráveis

---

## 📚 Conceitos Aplicados

Este projeto explora diversos conceitos introdutórios da criptografia:

- **Criptografia Simétrica:** mesma chave para encriptar e desencriptar.
- **Cifra por Substituição:** cada letra do texto original é substituída por outra.
- **Criptoanálise:** técnicas para decifrar mensagens sem conhecer a chave.
- **Ataque por força bruta:** tentativa de todas as chaves possíveis (neste caso, 25 tentativas).

---

## 🔐 Exemplo de Execução

```
=== Caesar Cipher Tool ===
1. Encrypt sample text
2. Encrypt your own text
3. Decrypt your own text
0. Exit

Enter your text: DEFEND THE EAST WALL OF THE CASTLE
Enter shift value (key k): 3

=== Encryption Result with shift value 3 ===
Original : DEFEND THE EAST WALL OF THE CASTLE
Encrypted: GHIHQG WKH HDVW ZDOO RI WKH FDVWOH
```

---

## 🧠 Sobre a Segurança da Cifra

Apesar de histórica, a Cifra de César **não é segura para uso moderno**:

- Existem apenas 25 chaves possíveis (deslocamentos de 1 a 25).
- Pode ser quebrada facilmente por tentativa e erro ou análise de frequência.
- Serve como excelente exemplo didático para introdução à criptografia.

---