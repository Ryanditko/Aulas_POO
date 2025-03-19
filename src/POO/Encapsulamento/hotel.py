class hospede:
    def __init__(self, nome:str, quarto:Quarto, conta:Conta):
        self.__nome = nome
        self.__Quarto = quarto
        self.__Conta = conta 
    
    def fazer_check_in(self, quarto:Quarto):
        self.__Quarto = quarto
        
    def fazer_check_out(self):
        self.

    def pagar_conta(self):
        
    
    def pedir_comida(self, chef:Chefe, nome:str):