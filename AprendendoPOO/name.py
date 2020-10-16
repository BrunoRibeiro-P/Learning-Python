#--> Serve para não dar bug para o modulo que tiver dentro
# seja executado no modulo também.

def soma(x: float, y: float):
    return x + y

if __name__ == '__main__':
    print(soma(10, 20))
    print(soma(20, 20))