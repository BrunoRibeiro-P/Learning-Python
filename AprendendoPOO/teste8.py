class DidaticaTech:

    def __init__(self, v=10, i=1):
        self.valor = v
        self.incremento = i
        self.valor_exponencial = v

    def incrementa(self):
        self.valor += self.incremento

# Herança

class Calculos(DidaticaTech):

    def __init__(self, d=5):
        self.divisor = d
# polimorfismo(Classes com herança podem invocar metodos que tem a mesma assinatura
# mas comportamentos distintos.

    def decrementa(self):
        self.valor -= self.incremento

    def divide(self):
        self.valor = self.valor/self.divisor

c = Calculos()
c.decrementa()
c.divide()
print(c.valor)
