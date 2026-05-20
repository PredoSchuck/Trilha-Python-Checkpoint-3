import os
import time

def limpar_console():
    os.system("cls" if os.name == "nt" else "clear")

def carregar():
    time.sleep(3)

def quebra_linha():
    print("*" * 45)

def pausa_leitura():
    print(f"* {'Aperte a tecla ENTER para continuar':<41} *")
    input("*" * 45)

def opcao_invalida():
    quebra_linha()
    print(f"* {'Erro: Opção inválida. Tente novamente!':<41} *")
    quebra_linha()
    carregar()
    limpar_console()

def carregar_criacao_cadastro():
    print("Criando sua conta", end = "", flush = True)
    for _ in range(3):
        time.sleep(1)
        print(".", end = "", flush = True)
    print()

def carregar_criacao_conta():
    print("Criando sua conta", end = "", flush = True)
    for _ in range(3):
        time.sleep(1)
        print(".", end = "", flush = True)
    print()

def encerrar():
    quebra_linha()
    print(f"* {'Obrigado por usar nosso banco!':<41} *")
    print(f"* {'Volte sempre!!!':<41} *")
    quebra_linha()