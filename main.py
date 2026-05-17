from models.Cliente import Cliente
from models.ContaCorrente import ContaCorrente
from models.ContaPoupanca import ContaPoupanca
import view.menus as menus
import view.utilidades as util


while True:
    opcao = menus.menu_inicial()

    match(opcao):
        case "1":
            # CADASTRO CLIENTE
            pass
        case "2":
            opcao_conta = menus.criar_conta()
            match(opcao_conta):
                case "1":
                    # CADASTRO CONTA CORRENTE
                    util.carregar_criacao_conta()
                    pass
                case "2":
                    # CADASTRO CONTA POUPANÇA
                    util.carregar_criacao_conta()
                case _:
                    util.opcao_invalida()
        case "3":
            # ACESSAR CONTA
            pass
        case "4":
            # DÚVIDAS E SUGESTÕES
            pass
        case "5":
            # ENCERRAR CÓDIGO OK
            util.encerrar()
            break