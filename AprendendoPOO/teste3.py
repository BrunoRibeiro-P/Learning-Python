class DidaticaTech:
    def incrementa(self, v, i):
        self.valor = v
        self.incremento = i
        self.resultado = self.valor + self.incremento
        return self.resultado

a = DidaticaTech()
b = a.incrementa(10, 1)
print(a.incremento)