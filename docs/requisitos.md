# Requisitos do Sistema

## Objetivo

O sistema tem como objetivo auxiliar a AMA - Escola de Música Gospel no gerenciamento de alunos, professores, matrículas, aulas, presença, disponibilidade de professores e pagamentos.

## Perfis de Usuário

### Administrador

Usuário responsável pela gestão geral da escola.

Permissões:

- cadastrar alunos;
- cadastrar professores;
- criar matrículas;
- agendar aulas;
- acompanhar presença e faltas;
- controlar pagamentos;
- visualizar a agenda geral.

### Professor

Usuário responsável por acompanhar suas aulas e disponibilidade.

Permissões:

- visualizar suas aulas;
- cadastrar disponibilidade;
- marcar presença ou falta dos alunos;
- visualizar alunos vinculados às suas aulas.

### Aluno ou Responsável

Usuário responsável por acompanhar as informações do aluno.

Permissões:

- visualizar aulas marcadas;
- confirmar presença;
- visualizar status da matrícula;
- visualizar status de pagamento.

## Requisitos Funcionais

RF01 - O sistema deve permitir login de usuários.

RF02 - O sistema deve permitir diferentes perfis de usuário: administrador, professor e aluno/responsável.

RF03 - O sistema deve permitir o cadastro de alunos.

RF04 - O sistema deve permitir listar, editar e visualizar detalhes dos alunos.

RF05 - O sistema deve permitir o cadastro de professores.

RF06 - O sistema deve permitir listar, editar e visualizar detalhes dos professores.

RF07 - O sistema deve permitir cadastrar a disponibilidade semanal dos professores.

RF08 - O sistema deve permitir criar matrículas para alunos.

RF09 - O sistema deve permitir agendar aulas vinculando aluno, professor, instrumento, data e horário.

RF10 - O sistema deve permitir alterar o status de uma aula.

RF11 - O sistema deve permitir registrar presença ou falta do aluno.

RF12 - O sistema deve permitir consultar o histórico de aulas de um aluno.

RF13 - O sistema deve permitir consultar a agenda de um professor.

RF14 - O sistema deve permitir registrar pagamentos de mensalidades.

RF15 - O sistema deve permitir consultar pagamentos pendentes, pagos e atrasados.

RF16 - O sistema deve permitir registrar confirmação de presença antes da aula.

## Requisitos Não Funcionais

RNF01 - O sistema deve ser web.

RNF02 - O sistema deve possuir interface simples e responsiva.

RNF03 - O sistema deve proteger rotas que exigem login.

RNF04 - O sistema deve armazenar os dados em banco de dados.

RNF05 - O sistema deve ter código organizado em frontend e backend.

RNF06 - O sistema deve utilizar controle de versão com Git e GitHub.

RNF07 - O sistema deve possuir documentação do projeto.

RNF08 - O sistema deve ser desenvolvido pensando em manutenção futura.
