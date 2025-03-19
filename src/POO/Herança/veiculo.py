class Veiculo:
    def __init__(self, marca:str, modelo:str, placa:str):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa 

class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa)
        self.portas = portas

    def exibir(self):
        print('------------------')
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Placa:', self.placa)
        print('Portas:', self.portas)

# Programa Principal
carro1 = Carro('Ford', 'Ka', 'AAA-1234', 4)
carro.exibir()