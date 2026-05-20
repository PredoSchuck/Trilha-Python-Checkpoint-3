from datetime import datetime
from models import Cliente, ContaCorrente, ContaPoupanca
from views import menus, utilidades as util

class ContaController:
    def __init__(self):
        self.banco_clientes = {}

    def verificar_maioridade(self, data_str):
        try:
            data_nascimento = datetime.strptime(data_str.strip(), "%d/%m/%Y").date()
            hoje = datetime.today().date()

            idade = hoje.year - data_nascimento.year
            if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1

            if idade >= 18:
                return True, idade
            else:
                return False, f"Menor de idade: {idade} anos."
        except ValueError:
            return False, "Formato inválido! Use DD/MM/AAAA."

    def cadastrar_cliente(self):
        while True:
            util.limpar_console()
            nome, cpf, data_nascimento = menus.preencher_cliente()

            nome = nome.strip() if nome else ""
            cpf = cpf.strip() if cpf else ""
            data_nascimento = data_nascimento.strip() if data_nascimento else ""

            if not nome or not cpf or not data_nascimento:
                util.quebra_linha()
                print(f"* {'Erro: Todos os dados são obrigatórios!':<41} *")
                util.quebra_linha()
                util.pausa_leitura()
                continue

            if not cpf.isdigit():
                util.quebra_linha()
                print(f"* {'Erro: O CPF deve conter apenas números!':<41} *")
                util.quebra_linha()
                util.pausa_leitura()
                continue

            if cpf in self.banco_clientes:
                util.quebra_linha()
                print(f"* {'Erro: Este CPF já está cadastrado!':<41} *")
                util.quebra_linha()
                util.pausa_leitura()
                continue

            valido, resultado = self.verificar_maioridade(data_nascimento)

            if not valido:
                util.quebra_linha()
                texto_erro = f"Erro: {resultado}"
                print(f"* {texto_erro:<41} *")
                util.quebra_linha()
                util.pausa_leitura()
                continue

            novo_cliente = Cliente(nome, cpf, data_nascimento)
            self.banco_clientes[cpf] = novo_cliente
            
            util.quebra_linha()
            util.carregar_criacao_conta()
            util.limpar_console()
            
            util.quebra_linha()
            texto_sucesso = f"Cliente cadastrado!"
            print(f"* {texto_sucesso[:41]:^41} *")
            util.quebra_linha()
            util.pausa_leitura()
            break