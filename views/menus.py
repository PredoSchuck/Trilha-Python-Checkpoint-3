import config
from . import utilidades as util

def menu_inicial():
    util.limpar_console()
    util.quebra_linha()
    print(f"* {'Banco Genérico':^41} *")
    util.quebra_linha()
    print(f"* {'Bem vindo ao Banco Genérico!':<41} *")
    print(f"* {'Aqui você organiza o seu dinheiro da':<41} *")
    print(f"* {'melhor forma, da sua maneira!!!':<41} *")
    util.quebra_linha()
    print(f"* {'Como podemos ajudar você hoje?':<41} *")
    print(f"* {'1 - Cadastro de cliente':<41} *")
    print(f"* {'-> Selecione aqui, para o primeiro uso no':<41} *")
    print(f"* {'   nosso banco.':<41} *")
    print(f"* {'-> Um CPF por cliente!':<41} *")
    print(f"* {'2 - Criar conta':<41} *")
    print(f"* {'-> Selecione aqui, caso já tenha um':<41} *")
    print(f"* {'   cadastro como cliente.':<41} *")
    print(f"* {'3 - Acessar conta':<41} *")
    print(f"* {'-> Selecione aqui, caso já tenha uma':<41} *")
    print(f"* {'   conta':<41} *")
    print(f"* {'4 - Dúvidas e Sugestões':<41} *")
    print(f"* {'-> Fale com conosco!':<41} *")
    print(f"* {'0 - Encerrar sistema':<41} *")
    util.quebra_linha()
    opcao = input("* ")
    util.limpar_console()
    return opcao

def criar_cliente():
    util.quebra_linha()
    print(f"* {'Cadastro de CPF':^41} *")
    util.quebra_linha()
    print(f"* {'1 - Cadastro de CPF':<41} *")
    print(f"* {'0 - Sair':<41} *")
    util.quebra_linha()
    print(f"* {'Obs: Em breve teremos conta para CNPJ':<41} *")
    util.quebra_linha()
    opcao = input("* ")
    util.limpar_console()
    return opcao

def preencher_cliente():
    util.quebra_linha()
    print(f"* {'Cadastro de CPF':^41} *")
    util.quebra_linha()
    print(f"* {'Qual o seu nome completo?':<41} *")
    nome = input("* ").strip()
    print(f"* {'Qual seu CPF? (Apenas números)':<41} *")
    cpf = input("* ").strip()
    print(f"* {'Qual sua data de nascimento?':<41} *")
    data_nascimento = input("* ").strip()
    return nome, cpf, data_nascimento

def criar_conta():
    util.limpar_console()
    util.quebra_linha()
    print(f"* {'Qual o tipo de conta que deseja abrir?':<41} *")
    print(f"* {'1 - Conta Corrente':<41} *")
    txt_taxa = f"-> Cobramos uma taxa de R$ {config.TAXA_SAQUE:.2f} para cada"
    print(f"* {txt_taxa:<41} *")
    print(f"* {'   saque realizado.':<41} *")
    print(f"* {'-> É possível sacar quando quiser.':<41} *")
    
    print(f"* {'2 - Conta Poupança':<41} *")
    txt_juros = f"-> Rende {config.JUROS_POUPANCA * 100:.1f}% no mês"
    print(f"* {txt_juros:<41} *")
    print(f"* {'-> Apenas 3 saques no mês':<41} *")
    print(f"* {'0 - Sair':<41} *")
    util.quebra_linha()
    opcao = input("* ")
    util.limpar_console()
    return opcao

def menu_conta():
    print("*-------------------------------------------*")
    print(f"* {'Cadastro de Conta':^41} *")
    print("*-------------------------------------------*")
    print(f"* {'1 - Ver Saldo':<41} *")
    print(f"* {'2 - Depositar':<41} *")
    print(f"* {'3 - Sacar':<41} *")
    print(f"* {'0 - Sair':<41} *")
    print(f"* {'Escolha uma opção acima:':<41} *")
    util.quebra_linha()
    opcao = input("* ")
    util.limpar_console()
    return opcao