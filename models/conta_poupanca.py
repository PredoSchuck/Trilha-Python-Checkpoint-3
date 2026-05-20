from . import Conta
import config

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self.saques_realizados_mes = 0

    def render_juros(self):
        juros = config.JUROS_POUPANCA
        rendimento = self._saldo * juros
        self._saldo += rendimento
        print(f"Juros de R$ {rendimento:.2f} aplicados ao saldo!")