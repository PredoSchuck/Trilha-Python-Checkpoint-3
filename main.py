from Cliente import Cliente
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
import tarefas as t

print("Bem-vindo ao Sistema Bancário")
nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
cliente_usuario = Cliente(nome, cpf)

print("Qual conta deseja abrir?")
print("1 - Conta Corrente (Taxa de R$ 1,00 por saque)")
print("2 - Conta Poupança (Rendimento de 1%)")
tipo = input("Opção: ")

numero_conta = 1001
if tipo == "1":
    conta = ContaCorrente(numero_conta, cliente_usuario)
    print(f"Conta Corrente aberta para {cliente_usuario.nome}!")
else:
    conta = ContaPoupanca(numero_conta, cliente_usuario)
    print(f"Conta Poupança aberta para {cliente_usuario.nome}!")

while True:
    opcao = t.menu()

    if opcao == "1":
        print(f"Seu saldo atual é: R$ {conta.get_saldo():.2f}")
    
    elif opcao == "2":
        valor = float(input("Valor do depósito: R$ "))
        conta.depositar(valor)
    
    elif opcao == "3":
        valor = float(input("Valor do saque: R$ "))
        conta.sacar(valor)
    
    elif opcao == "0":
        print("Obrigado por usar o ATM. Até logo!")
        break
    else:
        print("Opção inválida.")