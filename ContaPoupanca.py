from Conta import Conta

juros = 0.01

class ContaPoupanca(Conta):
    def render_juros(self):
        global juros
        juros *= self._saldo
        self._saldo += juros
        print(f"Juros de R$ {juros:.2f} aplicados ao saldo!")