import config
import view.utilidades as util

def menu_inicial():
    util.limpar_console()
    print("*--------------Banco Genérico---------------*")
    print("* Bem vindo ao Banco Genérico!              *")
    print("* Aqui você organiza o seu dinheiro da      *")
    print("* melhor forma, da sua maneira!!!           *")
    util.quebra_linha()
    print("* Obervação! Só trabalhamos com CPF         *")
    util.quebra_linha()
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
    util.quebra_linha()
    opcao = input("* ")
    return opcao

def criar_conta():
    util.limpar_console()
    util.quebra_linha()
    print("* Qual o tipo de conta que deseja abrir?    *")
    print("* 1 - Conta Corrente                        *")
    print(f"* -> Cobramos uma taxa de R$ {config.TAXA_SAQUE:.2f} para cada *")
    print("* saque realizado.                          *")
    print("* -> É possível sacar quando quiser.        *")
    print("* 2 - Conta Poupança                        *")
    print(f"* -> Rende {config.JUROS_POUPANCA * 100}% no mês                      *")
    print("* -> Apenas 3 saques no mês                 *")
    opcao = input("* ")
    util.limpar_console()
    return opcao


def menu_conta():
    print("*-------------------Conta-------------------*")
    print("* 1 - Ver Saldo                             *")
    print("* 2 - Depositar                             *")
    print("* 3 - Sacar                                 *")
    print("* 0 - Sair                                  *")
    print("* Escolha uma opção acima:                  *")
    util.quebra_linha()
    return input("* ")