class Produto:
    def __init__(self,nome:str,preco:float,quantidade:int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Pedido:
    def __init__(self):
        self.produtos: list[Produto] = []

    def adicionar_produto(self,produto:Produto):
        self.produtos.append(produto)
    
    def calcular_valor(self):
        valor_total = 0
        for produto in self.produtos:
            valor_total += produto.preco * produto.quantidade
        return valor_total
        
# Programa principal
cafe = Produto('Café solúvel', 5.50, 1)
arroz = Produto('Arroz integral', 4.90, 2)
feijao = Produto('Feijão preto', 2.80, 2)

meu_pedido = Pedido()

meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)

print('O valor total é:', meu_pedido.calcular_valor())