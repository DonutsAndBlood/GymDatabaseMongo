MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Carregar templates
6 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Alunos
2 - Relatório de Exercicios
3 - Relatório de Exercicios Favoritos
4 - Relatório de Alunos Inadimplentes
0 - Sair
"""

MENU_ENTIDADES = """Escolha a entidade
1 - Alunos
2 - Exercicio
"""

# Consulta de contagem de registros por tabela
def query_count(collection_name):
   from conexion.mongo_queries import MongoQueries
   import pandas as pd

   mongo = MongoQueries()
   mongo.connect()

   my_collection = mongo.db[collection_name]
   total_documentos = my_collection.count_documents({})
   mongo.close()
   df = pd.DataFrame({f"total_{collection_name}": [total_documentos]})
   return df

def clear_console(wait_time:int=2):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")