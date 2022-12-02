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

    def get_relatorio_quant_pagamentos(self):

        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["alunos"].find({"Pagamento": "I"},{"Nome_Aluno": 1, "_id": 0})

        df_aluno = pd.DataFrame(list(query_result))

        mongo.close()
        print(df_aluno)
        input("Pressione Enter para Sair de alunos inadimplentes")

    def get_relatorio_exercicio_favorito(self):
        mongo = MongoQueries()
        mongo.connect()

        query_result = mongo.db["alunos"].aggregate([
                                                    {
                                                    "$lookup": {
                                                        "from": "exercicios",
                                                        "localField": "Alunos_Exercicios",
                                                        "foreignField": "Codigo_Exercicio",
                                                        "as": "Exercicio_Favorito"
                                                    }
                                                    },
                                                    {
                                                        "$unwind": {
                                                        "path": "$Exercicio_Favorito"
                                                        }
                                                    },
                                                    {
                                                   "$project": {
                                                        "_id": 0,
                                                        "Cpf": 0,
                                                        "Pagamento": 0,
                                                        "Vencimento_Mensalidade": 0,
                                                        "Telefone": 0,
                                                        "Alunos_Exercicios": 0,
                                                        "Exercicio_Favorito": {
                                                            "_id": 0,
                                                            "Codigo_Exercicio": 0,
                                                            "Repeticoes": 0,
                                                            "Grupo_Muscular": 0
                                                        }
                                                    }
                                                    }])
        df_aluno = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        mongo.close()
        # Exibe o resultado
        print(df_aluno)
        input("Pressione Enter para Sair do Relatório de Exercicios favoritos")
