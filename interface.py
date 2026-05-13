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

def menu_inicial():
    print("*--------------Banco Genérico---------------*")
    print("* Bem vindo ao Banco Genérico!              *")
    print("* Aqui você organiza o seu dinheiro da      *")
    print("* melhor forma, da sua maneira!!!           *")
    quebra_linha()
    print("* Obervação! Só trabalhamos com CPF         *")
    quebra_linha()
    print("* Como podemos ajudar você hoje?            *")
    print("* 1 - Cadastro de cliente                   *")
    print("* -> Selecione aqui, para o primeiro uso no *")
    print("*    nosso banco.                           *")
    print("* -> Um CPF por cliente!                    *")
    print("* 2 - Criar conta                           *")
    print("* -> Selecione aqui, caso já tenha um       *")
    print("*    cadastro como cliente.                 *")
    print("* 3 - Acessar conta                         *")
    print("* -> Selecione aqui, caso já tenha uma      *")
    print("*    conta                                  *")
    print("* 4 - Dúvidas e Sugestões                   *")
    print("* -> Fale com conosco!                      *")
    print("* 5 - Encerrar sistema                      *")
    opcao = input("* ")
    return opcao

def criar_conta():
    quebra_linha()
    print("* Qual o tipo de conta que deseja abrir?    *")
    print("* 1 - Conta Corrente                        *")
    print("* -> Cobramos uma taxa de R$ 1,00 para cada *")
    print("* saque realizado.                          *")
    print("* -> É possível sacar quando quiser.        *")
    print("* 2 - Conta Poupança                        *")
    print("* -> Rende 1% no mês                        *")
    print("* -> Apenas 3 saques no mês                 *")
    opcao = input("* ")
    limpar_console()
    return opcao

def carregar_criacao_conta():
    print("Criando sua conta", end = "", flush = True)
    for _ in range(3):
        time.sleep(1)
        print(".", end = "", flush = True)

def menu_principal():
    print("*--------------------ATM--------------------*")
    print("* 1 - Ver Saldo                             *")
    print("* 2 - Depositar                             *")
    print("* 3 - Sacar                                 *")
    print("* 0 - Sair                                  *")
    print("* Escolha uma opção acima:                  *")
    quebra_linha()
    return input("* ")

def encerrar():
    print("* Obrigado por usar nosso banco!            *")
    print("* Volte sempre!!!                           *")
    quebra_linha()