from Conta import Conta

taxa = 1.0

class ContaCorrente(Conta):
    def sacar(self, valor):
        global taxa
        saque = valor + taxa
        if saque <= self._saldo:
            self._saldo -= saque
            print(f"Saque de R$ {valor:.2f} realizado (taxa: R$ {taxa:.2f}).")
            return True
        else:
            print(f"Saldo nsuficiente para cobrir o saque e a taxa de R$ {taxa:.2f}.")
            return False