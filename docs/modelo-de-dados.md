# Modelo de Dados

## Usuário

Representa uma pessoa que pode acessar o sistema.

### Campos

- id
- nome
- email
- senha
- tipo_usuario
- criado_em

### Tipos de usuário

- administrador
- professor
- responsavel

---

## Responsável

Representa o pai, mãe ou responsável por um aluno.

### Campos

- id
- usuario_id
- nome
- telefone
- email
- criado_em

---

## Aluno

Representa um aluno matriculado na escola.

### Campos

- id
- responsavel_id
- nome
- data_nascimento
- telefone
- criado_em

---

## Instrumento

Representa um instrumento ensinado pela escola.

### Campos

- id
- nome

### Exemplos

- Piano
- Violão
- Guitarra
- Bateria
- Canto

---

## Professor

Representa um professor da escola.

### Campos

- id
- usuario_id
- nome
- telefone
- criado_em

---

## ProfessorInstrumento

Representa quais instrumentos um professor ensina.

### Campos

- id
- professor_id
- instrumento_id

---

## Matrícula

Representa o vínculo entre aluno, instrumento e professor.

### Campos

- id
- aluno_id
- professor_id
- instrumento_id
- status
- data_inicio
- data_fim
- valor_mensalidade
- criado_em

### Status da matrícula

- ativa
- pausada
- cancelada
- concluida

---

## Disponibilidade

Representa os horários disponíveis de um professor.

### Campos

- id
- professor_id
- dia_semana
- horario_inicio
- horario_fim

---

## Aula

Representa uma aula agendada.

### Campos

- id
- matricula_id
- aluno_id
- professor_id
- instrumento_id
- data
- horario_inicio
- horario_fim
- status
- confirmada_pelo_responsavel
- observacoes

### Status da aula

- marcada
- confirmada
- realizada
- falta
- cancelada
- remarcada

---

## Remarcação

Representa uma solicitação de remarcação de aula feita pelo responsável, professor ou administrador.

### Campos

- id
- aula_id
- solicitante_id
- nova_data
- novo_horario_inicio
- novo_horario_fim
- status
- motivo
- criado_em

### Status da remarcação

- pendente
- aprovada
- recusada

---

## Pagamento

Representa uma cobrança mensal do aluno.

### Campos

- id
- aluno_id
- matricula_id
- valor
- mes_referencia
- vencimento
- data_pagamento
- forma_pagamento
- status
- observacoes

### Status do pagamento

- pago
- pendente
- atrasado
- cancelado

### Formas de pagamento

- pix
- dinheiro
- cartão
- boleto
- transferência

---

## Notificação

Representa uma notificação enviada ao responsável, aluno ou professor.

### Campos

- id
- usuario_id
- tipo
- mensagem
- canal
- status
- criado_em

### Canais

- sistema
- whatsapp
- email

### Tipos

- lembrete_aula
- confirmacao_aula
- pagamento_pendente
- remarcacao
