# Sistema de Gerenciamento de Academia

````md
# Sistema de Gerenciamento de Academia

Projeto desenvolvido em Python para gerenciamento simples de alunos de uma academia via terminal.

O sistema permite:

- Cadastro de alunos
- Controle de status
- Registro de check-in
- Histórico de sessões
- Organização por modalidade
- Fila de atendimento (FIFO)
- Histórico de treinos (LIFO)
- Exclusão de alunos

---

# Tecnologias Utilizadas

- Python 3
- Estruturas de Dados:
  - Lista
  - Fila (FIFO)
  - Pilha (LIFO)
- Modularização em arquivos `.py`

---

# Estrutura do Projeto

```bash
📁 projeto-academia
│
├── main.py        # Arquivo principal do sistema
├── alunos.py      # Funções relacionadas aos alunos
├── dados.py       # Armazenamento das estruturas de dados
├── utils.py       # Funções auxiliares
└── README.md
````

---

# Funcionalidades do Sistema

## 1 Cadastrar Aluno

Permite cadastrar um novo aluno informando:

* Nome
* Modalidade
* Dias por semana
* Objetivo

Cada aluno recebe:

* ID único
* Status inicial = Ativo
* Histórico de sessões
* Total de sessões

---

## 2 Listar Alunos Ativos

Exibe apenas alunos com status:

✅ Ativo

Mostra:

* ID
* Nome
* Modalidade
* Objetivo
* Quantidade de sessões

---

## 3 Fila de Atendimento (FIFO)

O sistema utiliza uma fila FIFO:

> First In, First Out

O primeiro aluno que entra na fila é o primeiro a ser atendido.

### Exemplo:

```text
João entrou primeiro
Maria entrou depois

→ João será atendido primeiro
```

Os alunos entram na fila ao realizar check-in.

---

## 4 Registrar Check-in

Registra:

* Data
* Modalidade
* Duração do treino

Além disso:

* Adiciona sessão ao histórico
* Incrementa total de sessões
* Adiciona aluno na fila de atendimento

---

## 5 Atualizar Status do Aluno

Permite alterar o status para:

* Ativo
* Suspenso
* Cancelado

O sistema também permite:

* Reativar alunos
* Cancelar alunos suspensos

---

## 6 Histórico de Sessões (LIFO)

O histórico funciona como pilha (LIFO):

> Last In, First Out

As sessões mais recentes aparecem primeiro.

### Exemplo:

```text
Treino 1
Treino 2
Treino 3

→ O treino 3 será exibido primeiro
```

---

## 7 Listar por Modalidade

Organiza os alunos por modalidade:

* Musculação
* HIIT
* Crossfit
* Zumba
* Fit Dance
* Jiu Jitsu
* Muay Thai
* Natação
* etc.

---

## 8 Deletar Aluno

Remove permanentemente um aluno do sistema.

Antes da exclusão o sistema exibe:

* Dados do aluno
* Modalidade
* Status
* Última sessão

Também remove o aluno da fila de atendimento caso exista.

---

# Estruturas de Dados Utilizadas

## Lista

Utilizada para armazenar todos os alunos.

```python
alunos = []
```

---

## Fila (FIFO)

Usada no atendimento presencial.

```python
fila_atendimento = []
```

Remoção:

```python
fila_atendimento.pop(0)
```

---

## Pilha (LIFO)

Usada no histórico de sessões.

As sessões mais recentes são exibidas primeiro utilizando:

```python
reversed(sessoes)
```

---

# Exemplo do Menu

```text
1. Cadastrar Aluno
2. Listar Alunos Ativos
3. Fila de Atendimento Presencial
4. Registrar Check-in de Treino
5. Atualizar Status do Aluno
6. Ver Histórico de Sessões por Aluno
7. Listar Alunos por Modalidade
8. DELETAR Aluno
9. Sair
```

---

# Melhorias Futuras

* Salvar dados em arquivo JSON
* Banco de dados SQLite
* Interface gráfica
* Login de administrador
* Relatórios em PDF
* Controle financeiro
* Sistema web com Flask ou Django

---

# Autor

Projeto desenvolvido para fins de estudo de:

* Python
* Estruturas de Dados
* Modularização
* Manipulação de listas, filas e pilhas

---

# Licença

Este projeto é livre para estudos e modificações.

```
Gustavo Sacomani Rafael
```
