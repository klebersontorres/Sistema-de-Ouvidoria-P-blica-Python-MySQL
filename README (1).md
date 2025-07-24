
# 🗣️ Sistema de Ouvidoria Pública — Python + MySQL

Este repositório apresenta um **sistema de ouvidoria robusto** desenvolvido com Python e MySQL, com foco em segurança, organização dos dados e facilidade de uso. O projeto simula um canal institucional para registro, consulta e gerenciamento de manifestações públicas de forma transparente.

---

## 🔍 Visão Geral

A ouvidoria é uma ferramenta fundamental para ouvir e registrar as demandas da sociedade. Este sistema oferece uma implementação funcional que pode ser utilizada em instituições públicas, privadas, acadêmicas ou como projeto de aprendizagem.

---

## ⚙️ Funcionalidades

- 📋 **Listar manifestações:** Consulta todas as manifestações armazenadas no banco.
- 📝 **Inserção de manifestações:** Recebe dados via terminal, valida e insere no banco.
- 🔍 **Pesquisa avançada:** Permite busca por protocolo (15 dígitos), código ou tipo.
- 📊 **Contagem:** Exibe o número total de manifestações cadastradas.
- 🗑️ **Exclusão:** Permite cancelar manifestações por código.
- 🚪 **Encerramento controlado:** Fecha a conexão com segurança ao sair.

---

## 🔐 Segurança e Confiabilidade

- ✅ **Prepared Statements:** Todas as operações de banco utilizam comandos preparados, evitando SQL Injection.
- 🔁 **Rollback em caso de erro:** Em qualquer falha de inserção, atualização ou exclusão, a transação é revertida.
- ⚠️ **Mensagens de erro controladas:** Tratamento de exceções do MySQL para cada operação.
- 🔍 **Validações de entrada:** Protocolo com 15 dígitos, código apenas numérico, tipo obrigatório.

---

## 💡 Tecnologias Utilizadas

- **Python 3.x**  
- **MySQL**  
- **Biblioteca:** `mysql.connector`

---

## 📁 Estrutura do Projeto

```
├── menu.py                # Interface principal e controle de execução
├── ouvidoria.py           # Operações de negócio sobre manifestações
├── operacoesbd.py         # Módulo de acesso ao banco com abstração CRUD
└── README.md              # Descrição e orientações do projeto
```

---

## 🔧 Setup e Execução

1. **Configure o banco de dados MySQL:**
   ```sql
   CREATE DATABASE myouvidoria;
   USE myouvidoria;

   CREATE TABLE ouvidoria (
       codigo INT AUTO_INCREMENT PRIMARY KEY,
       nome VARCHAR(100),
       protocolo VARCHAR(15),
       tipoManifestacao VARCHAR(100),
       manifestacao TEXT
   );
   ```

2. **Clone o repositório e execute o projeto:**
   ```bash
   git clone https://github.com/klebersontorres/Sistema-de-Ouvidoria-Publica-Python-MySQL.git
   cd Sistema-de-Ouvidoria-Publica-Python-MySQL
   python menu.py
   ```

---

## 🖼️ Exemplo de Execução

> Após clonar e rodar o sistema, sua interface no terminal se parecerá com:

![Exemplo terminal](docs/exemplo_terminal.png)

Crie uma pasta `docs/` e adicione uma captura de tela com esse nome para exibição automática no GitHub.

---

## ✨ Destaques Técnicos

- Modularização do código (separação em três arquivos principais).
- CRUD completo com **abstração de acesso ao banco** (`operacoesbd.py`).
- Interface de linha de comando interativa com opções enumeradas.
- Projeto ideal para fins acadêmicos, avaliação de portfólio e expansão para Web/API futuramente.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues, fazer forks e enviar *pull requests*.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
