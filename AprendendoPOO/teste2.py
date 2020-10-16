class DidaticaTech: # funções usa letras minúsculas e classes úsa maiusculas

    def incrementa(self, v, i): #método função dentro da classe
        valor = v #variaveis dentro das classes são atributos
        incremento = i
        resultado = valor + incremento
        return resultado

#a = DidaticaTech()
#print(a.incrementa(10, 1))
print(DidaticaTech().incrementa(10, 1))
#print(valor) --> Não funciona, pois precisa do self