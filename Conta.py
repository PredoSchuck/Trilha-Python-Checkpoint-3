class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self._saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
            return True
        else:
            print("Valor de saque inválido.")
            return False

    def get_saldo(self):
        return self._saldo