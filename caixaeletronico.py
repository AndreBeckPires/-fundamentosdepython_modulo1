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

# Função para exibir o menu e permitir que o usuário escolha a operação
def menu():
    
    
    while True:
        print("\nEscolha uma operação:")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == "1":
            print(f"Saldo atual: R${caixa.ver_saldo()}")
        
        elif opcao == "2":
            try:
                valor_deposito = float(input("Digite o valor a ser depositado: R$"))
                caixa.deposito(valor_deposito)
            except ValueError:
                print("Valor inválido! Digite um número válido.")
        
        elif opcao == "3":
            try:
                valor_saque = float(input("Digite o valor a ser sacado: R$"))
                caixa.saque(valor_saque)
            except ValueError:
                print("Valor inválido! Digite um número válido.")
        
        elif opcao == "4":
            print("Saindo... Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# volta para o inicio

