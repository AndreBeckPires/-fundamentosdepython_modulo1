#class CaixaEletronico():
 #   saldo = 0
    
  #  def verSaldo(self):
   #     return self.saldo
    #cx = CaixaEletronico()
    #cx.verSaldo()
#saque = 
#deposito = 
class CaixaEletronico:

    usuario = ''
    def __init__(self,valor,user):
        self.usuario = user
        #Inicializa o saldo do caixa eletrônico como 0.
        self.saldo = valor
    
    def ver_saldo(self):
        #Retorna o saldo atual.
        return self.saldo
    
    def deposito(self, valor):
        #Realiza um depósito no saldo, se o valor for positivo.
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Valor de depósito inválido. O valor deve ser maior que zero.")
    
    def saque(self, valor):
        #Realiza um saque, se o saldo for suficiente.
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")


