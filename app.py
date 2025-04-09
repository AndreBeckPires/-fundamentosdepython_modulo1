import manageusers
import caixaeletronico


while manageusers.success != 1:
    manageusers.selectAction()

#loop principal
if(manageusers.getAutenticado() == 1):
    usuario =  caixaeletronico.CaixaEletronico(30,manageusers.getUser())
    print(f'Conectado como {usuario.usuario}')

while manageusers.getAutenticado() == 1:

    print("\nEscolha uma operação:")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")
    print("5. Encerrar")
        
    opcao = input()
        
    if opcao == "1":
            print(f"Saldo atual: R${usuario.ver_saldo()}")
        
    elif opcao == "2":
        try:
            valor_deposito = float(input("Digite o valor a ser depositado: R$"))
            usuario.deposito(valor_deposito)
        except ValueError:
            print("Valor inválido! Digite um número válido.")
        
    elif opcao == "3":
        try:
            valor_saque = float(input("Digite o valor a ser sacado: R$"))
            usuario.saque(valor_saque)
        except ValueError:
            print("Valor inválido! Digite um número válido.")
    elif opcao == "4":
        print("Deslogando")
        manageusers.logout()
        manageusers.selectAction()
    elif opcao == "5":
        print("Saindo... Até logo!")
        exit()
        break
        
    else:
        print("Opção inválida! Tente novamente.")#action = input()
    #if action == '1':
     #   manageusers.logout()
        #manageusers.selectAction()
    #if action == '2':
     #   exit()
    
    