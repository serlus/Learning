
# Atividade para Candidatos - Mastertech

Esse documento apresenta uma descrição de requisitos para criação do sistema. Os requisitos são apresentados em alto nível - isso é feito intencionalmente para permitir comque o candidato utilize sua capacidade de compreensão, modelagem e organização doprojeto. Qualquer ponto que não esteja descrito neste documento fica a critério do participante.

O código final deve ser disponibilizado em um repositório público no Github ou serviçosimilar. O link deve ser enviado para ​nsilva@mastertech.com.br​.

## Exercício Proposto

O exercício proposto é a criação de um sistema simples para controle de entrada e saída deuma empresa. O sistema deve permitir o cadastro de usuários e o registro de ponto dosmesmos.

### 1. Requisitos não-funcionais

1. O sistema deve ser desenvolvido em Python utilizando Flask e com suporte dasbibliotecas: SQLAlchemy, Alembic, Marshmallow e Mockito
2. O sistema deve ser uma API REST seguindo as melhores práticas do padrão
3. O formato de dados definido para a API é JSON
4. Para banco de dados, pode-se usar H2, SQLite, MySQL ou Postgres
5. O projeto deve conter ao menos 5 testes unitários e 5 testes de aceitação.
6. O projeto deve ter um readme com uma breve documentação dos endpoints da API2. 

### Requisitos Funcionais

#### 2.1 Gestão de Usuários
Atributos: ​id, nome completo, cpf, email e data de cadastro

**Operações possíveis**
 - **Criação​:** todos os atributos devem ser preenchidos, com exceção do id, que serágerado automaticamente no momento do cadastro.
 - **Edição​:** todos os campos são editáveis, com exceção do id e da data de cadastro.-Consulta​: deve-se exibir os dados de um usuário de acordo com id informado.
 - **Listagem​:** deve ser feita a listagem de todos os usuários cadastrados na base.

#### 2.2 Batidas de Ponto
 - **Atributos:​** id, usuário responsável pela batida, data/hora da batida e tipo da batida (entradaou saída)
Operações possíveis
 - **Criação​:** cadastro uma batida de ponto (seja entrada ou saída) para um usuário específico,de acordo com o id informado.
 - **Listagem​:** listagem de todas as batidas de ponto de um único usuário. Deve-se mostrar naresposta, além da lista de batidas, o total de horas trabalhadas.
