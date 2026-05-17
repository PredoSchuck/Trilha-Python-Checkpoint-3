import os
import time

def limpar_console():
    os.system("cls")

def carregar():
    time.sleep(3)

def pausa_leitura():
    print("* Aperte a tecla ENTER para continuar       *")
    input("*-------------------------------------------*")

def quebra_linha():
    print("*-------------------------------------------*")

def opcao_invalida():
    quebra_linha()
    print("* Opção inválida!!! Tente Novamente!!!      *")
    quebra_linha()
    carregar()
    limpar_console()
    
def carregar_criacao_conta():
    print("Criando sua conta", end = "", flush = True)
    for _ in range(3):
        time.sleep(1)
        print(".", end = "", flush = True)
        
def encerrar():
    print("* Obrigado por usar nosso banco!            *")
    print("* Volte sempre!!!                           *")
    quebra_linha()