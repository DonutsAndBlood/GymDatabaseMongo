db.createCollection("exercicios")

db.createCollection("alunos")

db.exercicios.insertMany([
{Codigo_Exercicio: 1, Repeticoes: 12, Nome_Exercicio: 'Voador', Grupo_Muscular: 'A'},
{Codigo_Exercicio: 2, Repeticoes: 12, Nome_Exercicio: 'Supino inclinado com barra', Grupo_Muscular: 'A'},
{Codigo_Exercicio: 3, Repeticoes: 12, Nome_Exercicio: 'Crucifixo reto', Grupo_Muscular: 'A'},
{Codigo_Exercicio: 4, Repeticoes: 11, Nome_Exercicio: 'Supino reto com barra', Grupo_Muscular: 'A'},
{Codigo_Exercicio: 5, Repeticoes: 10, Nome_Exercicio: 'Tr?ceps Voador', Grupo_Muscular: 'A'},
{Codigo_Exercicio: 6, Repeticoes: 10, Nome_Exercicio: 'Tr?ceps Corda Cross', Grupo_Muscular: 'A'},
{Codigo_Exercicio: 7, Repeticoes: 12, Nome_Exercicio: 'Polichinelo', Grupo_Muscular: 'A'},
{Codigo_Exercicio: 8, Repeticoes: 10, Nome_Exercicio: 'Flex?o', Grupo_Muscular: 'A'},
{Codigo_Exercicio: 9, Repeticoes: 11, Nome_Exercicio: 'Tr?ceps Barra Cross', Grupo_Muscular: 'A'},
{Codigo_Exercicio: 10, Repeticoes: 12, Nome_Exercicio: 'Tr?ceps Testa', Grupo_Muscular: 'A'},
{Codigo_Exercicio: 11, Repeticoes: 11, Nome_Exercicio: 'Levantamento terra', Grupo_Muscular: 'B'},
{Codigo_Exercicio: 12, Repeticoes: 12, Nome_Exercicio: 'Pulley Frontal', Grupo_Muscular: 'B'},
{Codigo_Exercicio: 13, Repeticoes: 11, Nome_Exercicio: 'Pulley Atr?s', Grupo_Muscular: 'B'},
{Codigo_Exercicio: 14, Repeticoes: 11, Nome_Exercicio: 'Remada Baixa', Grupo_Muscular: 'B'},
{Codigo_Exercicio: 15, Repeticoes: 12, Nome_Exercicio: 'Serrote', Grupo_Muscular: 'B'},
{Codigo_Exercicio: 16, Repeticoes: 10, Nome_Exercicio: 'Rosca Alternada com Banco inclinado', Grupo_Muscular: 'B'},
{Codigo_Exercicio: 17, Repeticoes: 11, Nome_Exercicio: 'Rosca Scott barra W', Grupo_Muscular: 'B'},
{Codigo_Exercicio: 18, Repeticoes: 10, Nome_Exercicio: 'Rosca direita barra Reta', Grupo_Muscular: 'B'},
{Codigo_Exercicio: 19, Repeticoes: 12, Nome_Exercicio: 'Martelo em p?', Grupo_Muscular: 'B'},
{Codigo_Exercicio: 20, Repeticoes: 11, Nome_Exercicio: 'Rosca Punho', Grupo_Muscular: 'B'},
{Codigo_Exercicio: 21, Repeticoes: 11, Nome_Exercicio: 'Leg press 45?', Grupo_Muscular: 'C'},
{Codigo_Exercicio: 22, Repeticoes: 12, Nome_Exercicio: 'Extensor de pernas', Grupo_Muscular: 'C'},
{Codigo_Exercicio: 23, Repeticoes: 10, Nome_Exercicio: 'Flexora Sentada', Grupo_Muscular: 'C'},
{Codigo_Exercicio: 24, Repeticoes: 12, Nome_Exercicio: 'Adutora', Grupo_Muscular: 'C'},
{Codigo_Exercicio: 25, Repeticoes: 12, Nome_Exercicio: 'Abdutora', Grupo_Muscular: 'C'},
{Codigo_Exercicio: 26, Repeticoes: 12, Nome_Exercicio: 'Stiff', Grupo_Muscular: 'C'},
{Codigo_Exercicio: 27, Repeticoes: 11, Nome_Exercicio: 'Desenvolvimento nuca com Barra', Grupo_Muscular: 'C'},
{Codigo_Exercicio: 28, Repeticoes: 12, Nome_Exercicio: 'Desenvolvimento Maquina', Grupo_Muscular: 'C'},
{Codigo_Exercicio: 29, Repeticoes: 11, Nome_Exercicio: 'Eleva??o frontal com halteres em p?', Grupo_Muscular: 'C'},
{Codigo_Exercicio: 30, Repeticoes: 11, Nome_Exercicio: 'Eleva??o lateral com halteres sentado', Grupo_Muscular: 'C'}
])

db.alunos.insertMany([
{Cpf: '954.206.637-67', Nome_Aluno: 'Pedro Henrique Bruno Danilo da Rosa', Pagamento: 'A', Vencimento_Mensalidade: 28, Alunos_Exercicios: 1, Telefone: 27984317939},
{Cpf: '271.716.287-95', Nome_Aluno: 'Ben?cio Bryan Sales', Pagamento: 'A', Vencimento_Mensalidade: 25, Alunos_Exercicios: 3, Telefone: 27984536300},
{Cpf: '754.213.007-22', Nome_Aluno: 'Arthur Lu?s Silva', Pagamento: 'A', Vencimento_Mensalidade: 27, Alunos_Exercicios: 1, Telefone: 27983320915},
{Cpf: '277.716.817-27', Nome_Aluno: 'Francisco Kaique Victor Silveira', Pagamento: 'A', Vencimento_Mensalidade: 30, Alunos_Exercicios: 2, Telefone: 27992422949},
{Cpf: '678.856.887-12', Nome_Aluno: 'Ant?nia Patr?cia Juliana Drumond', Pagamento: 'I', Vencimento_Mensalidade: 30, Alunos_Exercicios: 2, Telefone: 28999628749},
{Cpf: '015.744.507-00', Nome_Aluno: 'Jorge Tom?s Noah Santos', Pagamento: 'I', Vencimento_Mensalidade: 8, Alunos_Exercicios: 1, Telefone: 27982094019}])