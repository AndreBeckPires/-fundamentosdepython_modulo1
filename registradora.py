import csv
def atualizar_saldo(file, data):
    with open(file, 'r', newline='') as csvfile:
        new = []
        reader = csv.reader(csvfile)
        for row in reader:
            new.append(row)
   
    new[0] = data

    with open(file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in new:
            csvwriter.writerow(row)

def registrar_saque(file,value):
    operacao = ['Saque',value]
    with open(file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(operacao)

def registrarDeposito(file,value):
    operacao = ['Deposito',value]
    with open(file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(operacao)  

def mostrar_extrato(file):
    with open(file,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        saldo = 0
        i = 0
        for row in csvreader:
            if i != 0:
                print(f'Operação: {row[0]} | Valor: {row[1]} Reais')
            else:
                saldo = str({row[1]})
                saldo = saldo[2:-2]
            i+= 1
        print(f'Saldo atual: {saldo} Reais')

