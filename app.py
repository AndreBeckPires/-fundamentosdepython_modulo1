import manageusers
import caixaeletronico
import csv

def createObject():
    while manageusers.success != 1:
        manageusers.selectAction()

    if(manageusers.getAutenticado() == 1):
        print("Entrou")
        with open(f'{manageusers.getUser()}.csv', 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                global dados
                dados = row
    global usuario
    usuario =  caixaeletronico.CaixaEletronico(float(dados[1]),manageusers.getUser())
    print(f'Conectado como {usuario.usuario}')
    menu()


def menu():
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
                dados[1] = usuario.ver_saldo()
                with open(f'{manageusers.getUser()}.csv', 'w', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(dados)
            except ValueError:
                print("Valor inválido! Digite um número válido.")
            
        elif opcao == "3":
            try:
                valor_saque = float(input("Digite o valor a ser sacado: R$"))
                usuario.saque(valor_saque)
                dados[1] = usuario.ver_saldo()
                with open(f'{manageusers.getUser()}.csv', 'w', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(dados)
            except ValueError:
                print("Valor inválido! Digite um número válido.")
        elif opcao == "4":
            print("Deslogando")
            manageusers.logout()
            manageusers.selectAction()
            createObject()
            break
        elif opcao == "5":
            print("Saindo... Até logo!")
            exit()
            
        else:
            print("Opção inválida! Tente novamente.")



createObject()
