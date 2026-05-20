from controllers import ContaController
from views import menus, utilidades as util

app = ContaController()

while True:
    opcao = menus.menu_inicial()
    match(opcao):
        case "1":
            opcao_cliente = menus.criar_cliente()
            match(opcao_cliente):
                case "1":
                    app.cadastrar_cliente()
                case "0":
                    continue
        case "2":
            opcao_conta = menus.criar_conta()
            match(opcao_conta):
                case "1":
                    pass
                case "2":
                    pass
                case _:
                    util.opcao_invalida()
        case "3":
            pass
        case "4":
            pass
        case "0":
            util.encerrar()
            break