from conexion.mongo_queries import MongoQueries
import pandas as pd
from pymongo import ASCENDING, DESCENDING

class Relatorio:
    def __init__(self):
        pass


    def get_relatorio_alunos(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["alunos"].find({}, 
                                                 {"Nome_Aluno": 1,
                                                  "Cpf": 1,
                                                  "Pagamento": 1,
                                                  "Vencimento_Mensalidade": 1,
                                                  "Alunos_Exercicios": 1,
                                                  "Telefone": 1,
                                                  "_id": 0
                                                 })#.sort("Nome_Aluno", ASCENDING) #Só não está ficando ASCENDING
        df_aluno = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_aluno)
        input("Pressione Enter para Sair do Relatório de Clientes")

            

    def get_relatorio_exercicios(self):
        # Cria uma nova conexão com o banco
        mongo = MongoQueries()
        mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = mongo.db["exercicios"].find({}, 
                                                 {"Codigo_Exercicio": 1,
                                                  "Repeticoes": 1, 
                                                  "Nome_Exercicio": 1,
                                                  "Grupo_Muscular": 1,
                                                  "_id": 0
                                                 })#.sort("Nome_Exercicio", ASCENDING) #Só não está ficando ASCENDING
        df_exercicio = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_exercicio)
        input("Pressione Enter para Sair do Relatório de Clientes")