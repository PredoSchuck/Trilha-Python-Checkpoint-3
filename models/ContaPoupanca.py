from Conta import Conta
import config

class ContaPoupanca(Conta):
    def render_juros(self):
        juros = config.JUROS_POUPANCA
        rendimento = self._saldo * juros
        self._saldo += rendimento
        print(f"Juros de R$ {rendimento:.2f} aplicados ao saldo!")