from Conta import Conta

class ContaPoupanca(Conta):
    def render_juros(self):
        juros = 0.01
        rendimento = self._saldo * juros
        self._saldo += rendimento
        print(f"Juros de R$ {rendimento:.2f} aplicados ao saldo!")