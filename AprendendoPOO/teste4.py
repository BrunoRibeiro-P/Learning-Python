class DidaticaTech:

    def __init__(self, v: int, i: int):# ou v=10 (Método construtor )
        self.valor = v
        self.incremento = i

    def incrementa(self):
        self.valor += self.incremento

a = DidaticaTech(1, 10)
b = a.incrementa()
print(a.valor) #Os valores só ficam salvos dentro do mesmo atributo

# Metódo = Compartilhado por todos da mesma classe
# Atributos = Não são compartilhado por todos da mesma classe, por isso o construror
# Metodos tem comportamentos iguais mais diferentes estados