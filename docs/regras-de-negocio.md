# Regras de Negócio

## RN01 - Perfis de usuário

O sistema deve possuir três perfis principais:

- Administrador
- Professor
- Aluno ou responsável

Cada perfil terá permissões diferentes dentro do sistema.

## RN02 - Cadastro de aluno

Todo aluno deve possuir, no mínimo:

- nome completo;
- data de nascimento;
- telefone de contato;
- responsável, caso seja menor de idade;
- status da matrícula.

## RN03 - Matrícula

Uma matrícula deve estar vinculada a um aluno.

A matrícula pode ter os seguintes status:

- ativa;
- pausada;
- cancelada;
- concluída.

## RN04 - Professor

Todo professor deve possuir:

- nome completo;
- telefone;
- instrumento(s) que ensina;
- disponibilidade semanal.

## RN05 - Disponibilidade do professor

O professor deve informar os dias e horários em que está disponível para dar aulas.

Uma aula só deve ser marcada em um horário disponível do professor.

## RN06 - Aula

Toda aula deve possuir:

- aluno;
- professor;
- instrumento;
- data;
- horário de início;
- horário de fim;
- status.

## RN07 - Status da aula

Uma aula pode ter os seguintes status:

- marcada;
- confirmada;
- realizada;
- falta;
- cancelada.

## RN08 - Controle de presença

Após a aula, o professor ou administrador deve registrar se o aluno compareceu ou faltou e deve enviar um relatório das aulas.

## RN09 - Pagamentos

O sistema deve permitir registrar o pagamento de mensalidades dos alunos.

Um pagamento pode ter os seguintes status:

- pago;
- pendente;
- atrasado.

## RN10 - Confirmação de aula

O sistema deve permitir registrar se o aluno ou responsável confirmou presença antes da aula.

Inicialmente, essa confirmação poderá ser feita manualmente pelo administrador.
