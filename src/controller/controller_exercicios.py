from model.Exercicios import Exercicios
import pandas as pd
from conexion.mongo_queries import MongoQueries
from reports.relatorio import Relatorio
from utils import config

relatorio = Relatorio()

class Controller_Exercicios:
    def __init__(self):
        self.mongo = MongoQueries()


    def inserir_exercicio(self) -> Exercicios:
        # Cria uma nova conexão com o banco que permite alteração
        while True:
            self.mongo.connect()

            print(self.listar_exercicios())
            nome_exercicio = input("Digite o nome do exercício: ")
            repeticoes = input("Número de repetições: ")
            grupo_muscular= input("Grupo muscular treinado: ")

            sequence = float(self.mongo.db["exercicios"].count_documents({})+1)

            
            # Insere e persiste o novo cliente
            self.mongo.db["exercicios"].insert_one({"Codigo_Exercicio": sequence, "Repeticoes": repeticoes,"Nome_Exercicio": nome_exercicio,"Grupo_Muscular": grupo_muscular})
            # Recupera os dados do novo cliente criado transformando em um DataFrame

            df_exercicio = self.recupera_exercicio(nome_exercicio)


            # Cria um novo objeto Cliente

            codigo = df_exercicio.Codigo_Exercicio.values[0]
            repeticoes = df_exercicio.Repeticoes.values[0]
            grupo_muscular = df_exercicio.Grupo_Muscular.values[0]
            nome = df_exercicio.Nome_Exercicio.values[0]


            novo_exercicio = Exercicios(codigo,repeticoes,grupo_muscular,nome)

            # Exibe os atributos do novo cliente
            print(novo_exercicio.to_string())
            self.mongo.close()
            # Retorna o objeto novo_cliente para utilização posterior, caso necessário

            print("Deseja continuar inserindo?")
            aux = int(input("""1 - Sim\n2 - Não\n"""))
            config.clear_console()

            if aux == 2:
                return novo_exercicio


            



    def atualizar_exercicio(self) -> Exercicios:
        while True:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect() 
            

            print(self.listar_exercicios())
            codigo_exercicio = float(input("Insira o código do exercício a ser alterado\n"))
            
            if not self.verifica_existencia_exercicio(codigo_exercicio):


                print("1 - Nome\n2 - Repetições")
                aux = int(input("Insira qual atributo irá ser alterado"))
                #Alterar nome      
                if aux == 1:

                    novo_nome = input("Insira o novo nome: ")

                    self.mongo.db["exercicios"].update_one({"Codigo_Exercicio": codigo_exercicio}, {"$set": {"Nome_Exercicio": novo_nome}})

                    df_exercicio = self.recupera_exercicio(novo_nome)

                    codigo = df_exercicio.Codigo_Exercicio.values[0]
                    repeticoes = df_exercicio.Repeticoes.values[0]
                    grupo_muscular = df_exercicio.Grupo_Muscular.values[0]
                    nome = df_exercicio.Nome_Exercicio.values[0]

                    exercicio_atualizado = Exercicios(codigo,repeticoes,grupo_muscular,nome)


                    print(exercicio_atualizado.to_string())

                    print("Deseja continuar alterando?")
                    aux = int(input("""1 - Sim\n2 - Não\n"""))
                    config.clear_console()

                    if aux == 2:
                        return exercicio_atualizado

                
                #Alterar Telefone
                elif aux == 2:

                    novo_repeticoes = input("Insira o novo número de repetições: ")


                    self.mongo.db["exercicios"].update_one({"Codigo_Exercicio": codigo_exercicio}, {"$set": {"Repeticoes": novo_repeticoes}})

                    df_exercicio = pd.DataFrame(list(self.mongo.db["exercicios"].find({"Codigo_Exercicio":codigo_exercicio}, {"Repeticoes": 1, "Codigo_Exercicio": 1,"Grupo_Muscular":1,"Nome_Exercicio":1, "_id": 0})))


                    codigo = df_exercicio.Codigo_Exercicio.values[0]
                    repeticoes = df_exercicio.Repeticoes.values[0]
                    grupo_muscular = df_exercicio.Grupo_Muscular.values[0]
                    nome = df_exercicio.Nome_Exercicio.values[0]
                    exercicio_atualizado = Exercicios(codigo,repeticoes,grupo_muscular,nome)
                

                    print(exercicio_atualizado.to_string())

                    print("Deseja continuar alterando?")
                    aux = int(input("""1 - Sim\n2 - Não\n"""))
                    config.clear_console()

                    if aux == 2:
                        return exercicio_atualizado
                



    def excluir_exercicio(self):
        while True:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

            print(self.listar_exercicios())
            codigo_exercicio = float(input("Codigo do exercicio a ser excluído: "))


            df_exercicio = pd.DataFrame(list(self.mongo.db["exercicios"].find({"Codigo_Exercicio":codigo_exercicio}, {"Repeticoes": 1, "Codigo_Exercicio": 1,"Grupo_Muscular":1,"Nome_Exercicio":1, "_id": 0})))

            # Solicita ao usuário o CPF do Cliente a ser alterado

            df_exercicio.to_string()
            # Verifica se o cliente existe na base de dados
            if not self.verifica_existencia_exercicio(codigo_exercicio):         

                # Recupera os dados do novo cliente criado transformando em um DataFrame

                self.mongo.db["exercicios"].delete_one({"Codigo_Exercicio":codigo_exercicio})

                codigo = df_exercicio.Codigo_Exercicio.values[0]
                repeticoes = df_exercicio.Repeticoes.values[0]
                grupo_muscular = df_exercicio.Grupo_Muscular.values[0]
                nome = df_exercicio.Nome_Exercicio.values[0]


                exercicio_excluido = Exercicios(codigo,repeticoes,grupo_muscular,nome)

                print("Exercicio removido com sucesso!")
                print(exercicio_excluido.to_string())

                print("Deseja continuar excluindo?")
                aux = int(input("""1 - Sim\n2 - Não\n"""))
                config.clear_console()
                if aux == 2:
                    return exercicio_excluido

            else:
                print(f"O codigo {codigo_exercicio} não existe.")

            

            
    def verifica_existencia_exercicio(self, codigo_exercicio:float=None, external:bool=False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_exercicio = pd.DataFrame(list(self.mongo.db["exercicios"].find({"Codigo_Exercicio":codigo_exercicio}, {"Repeticoes": 1, "Codigo_Exercicio": 1,"Grupo_Muscular":1,"Nome_Exercicio":1, "_id": 0})))   

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_exercicio.empty



    

    def recupera_exercicio(self, nome:str=None, external:bool=False) -> pd.DataFrame:

        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
            
        

        df_exercicio = pd.DataFrame(list(self.mongo.db["exercicios"].find({"Nome_Exercicio":f"{nome}"},{"Nome_Exercicio":1,"Codigo_Exercicio":1,"Repeticoes":1,"Grupo_Muscular":1, "_id":0})))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_exercicio



    def listar_exercicios(self, external:bool=False) -> bool:

        self.mongo.connect()
        # Recupera os dados transformando em um DataFrame
        query_result = self.mongo.db["exercicios"].find({}, 
                                                 {"Codigo_Exercicio": 1,
                                                  "Repeticoes": 1, 
                                                  "Nome_Exercicio": 1,
                                                  "Grupo_Muscular": 1,
                                                  "_id": 0
                                                 })#.sort("Nome_Exercicio", ASCENDING) #Só não está ficando ASCENDING
        df_exercicio = pd.DataFrame(list(query_result))
        # Fecha a conexão com o mongo
        # Exibe o resultado
        print(df_exercicio)
        
        