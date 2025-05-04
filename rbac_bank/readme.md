# 🛡️ RBAC - Controle de Acesso Baseado em Papéis

Este projeto simula um sistema bancário que implementa **Controle de Acesso Baseado em Papéis (RBAC - Role-Based Access Control)**, um dos principais modelos de controle de acesso utilizados em sistemas de informação.

## 📘 O que é RBAC?

O **RBAC (Role-Based Access Control)** é um modelo de controle de acesso que associa permissões a **papéis** e, por sua vez, os usuários são associados a esses papéis. Isso facilita a gestão de permissões, pois elas são concedidas aos papéis e não diretamente aos usuários.

Por exemplo, se um usuário deixa de ser gerente e se torna um cliente, basta trocar o papel, sem necessidade de alterar diretamente suas permissões.

---

## 🗂️ Estrutura do Projeto

O sistema é dividido nos seguintes arquivos:

- `main.py`: interface principal com o usuário.
- `auth.py`: responsável pela autenticação e recuperação do papel do usuário.
- `rbac.py`: define as permissões de cada papel e verifica autorizações.
- `bank_operations.py`: implementa as ações disponíveis no sistema.
- `data.py`: contém os dados dos usuários e seus papéis.
- `util.py`: funções auxiliares de interface.

---

## 👥 Papéis e Permissões

| Papel   | Permissões                              |
|---------|------------------------------------------|
| client  | `view_balance`, `view_statement`         |
| manager | `view_balance`, `view_statement`, `manage_accounts` |
| admin   | todas as anteriores + `create_user`      |

---

## 🧪 Como Testar

1. **Executar o programa principal:**

```bash
python main.py
```

2. **Fazer login com um dos usuários disponíveis:**

 ### 👤 Usuários disponíveis:

| Usuário | Senha      | Papel   |
|:-------:|:----------:|:-------:|
| rex     | client123  | client  |
| bob     | manager123 | manager |
| mel     | admin123   | admin   |


3. **Testar as opções disponíveis após login:**

As ações permitidas aparecerão no menu. Se o usuário tentar acessar uma função sem permissão, o sistema mostrará uma mensagem de "Access Denied".

---

## 🔐 Exemplo de Execução

```
=== Welcome to the International Bank System ===
Username: rex
Password:

[INFO] User 'rex' authenticated successfully.

=== Available Actions ===
1. View Balance
2. View Statement
3. Manage Accounts
4. Create User
q. Quit

Select an option: 3
Access Denied: You don't have permission to perform this action.
```

---

## 📚 Conceitos Relacionados

Este projeto é uma aplicação prática dos seguintes conceitos da disciplina de Gestão de Identidade e Acesso:

- **Autenticação Local:** login com usuário/senha armazenados localmente.
- **Autorização:** verificação de permissões com base no papel do usuário.
- **RBAC (Role-Based Access Control):** modelo onde permissões são atribuídas a papéis, e papéis a usuários.

---