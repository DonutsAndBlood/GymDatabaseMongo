from utils import config
from utils.splash_screen import SplashScreen
# from reports.relatorios import Relatorio
from reports.relatorio import Relatorio
from controller.controller_exercicios import Controller_Exercicios
from controller.controller_alunos import Controller_Alunos
import createCollectionsAndData
import json


tela_inicial = SplashScreen()
# relatorios = Relatorio()
relatorio = Relatorio()
ctrl_exercicio = Controller_Exercicios()
ctrl_aluno = Controller_Alunos()


def relatorios(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_alunos()          
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_exercicios()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_exercicio_favorito()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_quant_pagamentos()
        

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_aluno = ctrl_aluno.inserir_Aluno()
    elif opcao_inserir == 2:
        novo_exercicio = ctrl_exercicio.inserir_exercicio()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_alunos
        aluno_atualizado = ctrl_aluno.atualizar_aluno()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_exercicios
        exercicio_atualizado = ctrl_exercicio.atualizar_exercicio()


def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        ctrl_aluno.excluir_aluno()
    elif opcao_excluir == 2:                
        ctrl_exercicio.excluir_exercicio()



def run():

    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-6]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-5]: "))
            config.clear_console(1)
            relatorios(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [0-2]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [0-2]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4: #Excluir registros

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [0-2]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5: #carrega templates

            createCollectionsAndData.createCollections(True)
            createCollectionsAndData.inserts()

            config.clear_console(1)
            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 6:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado e bom treino!")
            exit(0)

        else:
            print("Opção inválida.")
            exit(1)

if __name__ == "__main__":
    run()