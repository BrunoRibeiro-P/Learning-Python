class DidaticaTech:

    def __init__(self, v=10, i=1):
        self.valor = v
        self.incremento = i
        self.valor_exponencial = v

    def incrementa(self):
        self.valor += self.incremento

class Calculos(DidaticaTech):

    def __init__(self, d=5): # --> método constutor 1
        super().__init__(v=10, i=1) # método construtor 2, novo que herda os atributos.
        self.divisor = d

    def decrementa(self):
        self.valor -= self.incremento

    def divide(self):
        self.valor = self.valor/self.divisor

c = Calculos()
c.incrementa()
c.decrementa()
c.divide()
print(c.valor)
