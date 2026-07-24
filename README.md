markdown# 💻 Sistema de Gerenciamento de Escala (Versão Terminal CLI)

Este documento é o guia oficial de requisitos e funcionalidades para o desenvolvimento do nosso sistema. O projeto será executado 100% via terminal (linha de comando), focando na lógica de programação e manipulação de dados na memória ou arquivos simples.

---

## 🚀 Funcionalidades para Desenvolver (Passo a Passo)

### 📌 Fase 1: Cadastros Básicos (Menu Principal)
O sistema deve exibir um menu numérico no terminal para cadastrar as informações na memória.
* **Cadastro de Colaboradores**: Opção para salvar Nome, Cargo e Carga Horária semanal.
* **Cadastro de Turnos**: Opção para salvar Nome do Turno, Horário de Entrada e Horário de Saída.
* **Listagem de Dados**: Opções no menu para exibir na tela todos os colaboradores e turnos cadastrados.

### 🗓️ Fase 2: Vínculo da Escala (A Lógica Principal)
* **Criar Escala**: O sistema pede o ID/Nome do colaborador e o ID/Nome do turno para vinculá-los a um dia da semana.
* **Visualizar Escala Geral**: Exibir no terminal a tabela completa da semana mostrando quem trabalha em qual turno.

### ⚠️ Fase 3: Validações Simples (Regras de Negócio)
* **Evitar Choque de Horário**: O sistema deve avisar se você tentar colocar o mesmo colaborador em dois turnos diferentes no mesmo dia.
* **Limite de Vagas**: Se um turno aceita apenas 3 pessoas, o sistema deve impedir o cadastro da 4ª pessoa e exibir um alerta.

---

## 📁 Estrutura de Dados Sugerida (Para Começar)

Como não usaremos banco de dados complexo, os dados podem ser armazenados em:
* **Listas / Dicionários / Arrays** na memória enquanto o programa estiver rodando.
* **Arquivos de Texto (.txt ou .json)** para salvar os dados permanentemente ao fechar o terminal (opcional/bônus).

---

## 🕹️ Exemplo de Como o Menu Deve Funcionar

```text
====== GERENCIADOR DE ESCALA ======
1. Cadastrar Colaborador
2. Cadastrar Turno
3. Montar Escala Semanal
4. Visualizar Escala Completa
0. Sair do Sistema
==================================
Escolha uma opção: _
```

---

## 🛠️ Tecnologias Recomendadas
* **Linguagens**: Python, JavaScript (Node.js) ou C#.
* **Interface**: Terminal / Console padrão.