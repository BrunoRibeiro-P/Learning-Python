class DidaticaTech:

    def __init__(self, v=10, i=1):
        self.valor = v
        self.incremento = i
        self.valor_exponencial = v

    def incrementa(self):
        self.valor += self.incremento

# Herança

class Calculos(DidaticaTech):

    pass
