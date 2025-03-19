class Triangulo:
    def __init__(self,a:float,b:float,c:float):
        self.lado_a=a
        self.lado_b=b
        self.lado_c=c

    def calcular_perimetro(self):
        perimetro = self.lado_a+self.lado_b+self.lado_c
        return perimetro

# Programa principal
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

t = Triangulo(a,b,c)
print(t.calcular_perimetro())
