# from Cliente import Cliente
# from ContaCorrente import ContaCorrente
# from ContaPoupanca import ContaPoupanca
# import interface as ui

# print("Bem-vindo ao Sistema Bancário")
# nome = input("Digite seu nome: ")
# cpf = input("Digite seu CPF: ")
# cliente_usuario = Cliente(nome, cpf)

# try:
#     print("Qual conta deseja abrir?")
#     print("1 - Conta Corrente (Taxa de R$ 1,00 por saque)")
#     print("2 - Conta Poupança (Rendimento de 1%)")
#     opcao_conta = input("Opção: ")
# except ValueError: 
#     print("Digite um número inteiro")

# numero_conta = 1001
# match(opcao_conta):
#     case "1":
#         conta = ContaCorrente(numero_conta, cliente_usuario)
#         print(f"Conta Corrente aberta para {cliente_usuario.nome}!")
#     case "2":
#         conta = ContaPoupanca(numero_conta, cliente_usuario)
#         print(f"Conta Poupança aberta para {cliente_usuario.nome}!")
#     case _:
#         ui.opcao_invalida



# while True:
#     opcao = ui.menu_principal()

#     if opcao == "1":
#         print(f"Seu saldo atual é: R$ {conta.get_saldo():.2f}")
    
#     elif opcao == "2":
#         valor = float(input("Valor do depósito: R$ "))
#         conta.depositar(valor)
    
#     elif opcao == "3":
#         valor = float(input("Valor do saque: R$ "))
#         conta.sacar(valor)
    
#     elif opcao == "0":
#         print("Obrigado por usar o ATM. Até logo!")
#         break
#     else:
#         print("Opção inválida.")

from Cliente import Cliente
from ContaCorrente import ContaCorrente as Corrente
from ContaPoupanca import ContaPoupanca as Poupanca
import interface as ui


while True:
    opcao = ui.menu_inicial()

    match(opcao):
        case "1":
            # CADASTRO CLIENTE
            pass
        case "2":
            opcao_conta = ui.criar_conta()
            match(opcao_conta):
                case "1":
                    # CADASTRO CONTA CORRENTE
                    ui.carregar_criacao_conta()
                    pass
                case "2":
                    # CADASTRO CONTA POUPANÇA
                    ui.carregar_criacao_conta()
                case _:
                    ui.opcao_invalida()
        case "3":
            # ACESSAR CONTA
            pass
        case "4":
            # DÚVIDAS E SUGESTÕES
            pass
        case "5":
            # ENCERRAR CÓDIGO OK
            ui.encerrar()
            break