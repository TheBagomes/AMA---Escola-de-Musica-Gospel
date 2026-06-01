# Planejamento do Projeto

## Objetivo

Desenvolver um sistema web para a AMA - Escola de Música Gospel, com foco em gestão de alunos, responsáveis, professores, matrículas, aulas, presença, pagamentos e notificações.

---

## Fase 1 - Fundação do Projeto

### Objetivo

Preparar a base técnica e documental do sistema.

### Tarefas

- Criar repositório no GitHub
- Criar documentação inicial
- Definir requisitos
- Definir regras de negócio
- Definir modelo de dados
- Definir stack do projeto
- Criar estrutura inicial do frontend
- Criar estrutura inicial do backend

### Status

Em andamento

---

## Fase 2 - Autenticação e Usuários

### Objetivo

Criar o sistema de login e permissões.

### Funcionalidades

- Login
- Cadastro de usuários
- Perfis de acesso:
  - administrador
  - professor
  - responsável
- Proteção de rotas
- Controle de permissões

---

## Fase 3 - Cadastros Principais

### Objetivo

Criar os cadastros básicos do sistema.

### Funcionalidades

- Cadastro de responsáveis
- Cadastro de alunos
- Cadastro de professores
- Cadastro de instrumentos
- Associação de professores com instrumentos

---

## Fase 4 - Matrículas

### Objetivo

Controlar o vínculo entre aluno, professor e instrumento.

### Funcionalidades

- Criar matrícula
- Vincular aluno a professor
- Vincular aluno a instrumento
- Definir valor da mensalidade
- Alterar status da matrícula
- Consultar matrículas ativas, pausadas, canceladas e concluídas

---

## Fase 5 - Agenda e Aulas

### Objetivo

Gerenciar a rotina de aulas da escola.

### Funcionalidades

- Cadastro de disponibilidade dos professores
- Agendamento de aulas
- Visualização da agenda geral
- Visualização da agenda por professor
- Confirmação de aula pelo responsável
- Cancelamento de aula
- Solicitação de remarcação
- Aprovação ou recusa de remarcação

---

## Fase 6 - Presença e Histórico

### Objetivo

Registrar a participação dos alunos nas aulas.

### Funcionalidades

- Marcar presença
- Marcar falta
- Registrar aula realizada
- Consultar histórico de aulas por aluno
- Consultar histórico de aulas por professor

---

## Fase 7 - Financeiro

### Objetivo

Permitir que a diretora acompanhe e gerencie pagamentos.

### Funcionalidades

- Registrar mensalidades
- Controlar pagamentos pagos, pendentes e atrasados
- Registrar forma de pagamento
- Registrar data de pagamento
- Consultar histórico financeiro do aluno
- Gerar visão geral financeira
- Permitir acesso apenas ao administrador

---

## Fase 8 - Notificações

### Objetivo

Automatizar lembretes e confirmações importantes.

### Funcionalidades

- Notificação de aula
- Confirmação um dia antes da aula
- Lembrete de pagamento pendente
- Notificação de remarcação
- Integração futura com WhatsApp
- Integração futura com e-mail

---

## Fase 9 - Deploy e Entrega

### Objetivo

Publicar o sistema para uso real.

### Tarefas

- Configurar ambiente de produção
- Configurar banco de dados em produção
- Publicar frontend
- Publicar backend
- Testar funcionalidades principais
- Criar documentação de uso
- Apresentar sistema para a escola

---

## MVP Inicial

A primeira versão funcional do sistema deve conter:

- Login
- Cadastro de responsáveis
- Cadastro de alunos
- Cadastro de professores
- Cadastro de instrumentos
- Matrículas
- Agenda de aulas
- Controle de presença
- Controle financeiro básico

---

## Funcionalidades Futuras

- Integração com WhatsApp
- Envio automático de lembretes
- Relatórios financeiros
- Dashboard administrativo
- Área completa do responsável
- Área completa do professor
- Exportação de dados
